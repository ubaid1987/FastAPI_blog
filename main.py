from fastapi import FastAPI, Depends
import schema, models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI(title="API App", description="My First Attempt", version="2.4.1")

# To Create DB Table
models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# To create a blog
@app.post("/blog", tags=["Blogs"], status_code=200)
def create(request: schema.Blog, db: Session = Depends(get_db)):
     new_blog = models.Blog(title=request.title, body=request.body, author=request.author)
     db.add(new_blog)
     db.commit()
     db.refresh(new_blog)
     return new_blog


# To get all blogs
@app.get('/blog', tags=["Blogs"], status_code=200)
def all(db: Session = Depends(get_db)):
    blog = db.query(models.Blog).all()
    return blog

# To get specific blog
@app.get('/blog/{id}', tags=["Blogs"], status_code=200)
def show(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    return blog


