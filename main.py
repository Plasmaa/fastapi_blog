from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    }
]

@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"posts":posts, "title": "Home"}, )


@app.get("/api/posts")
def get_posts():
    return posts

@app.get("/login", include_in_schema=False)
def login(request: Request):
    return templates.TemplateResponse(request, "login.html", {"title": "Login"})

@app.get("/register", include_in_schema=False)
def register(request: Request):
    return templates.TemplateResponse(request, "register.html", {"title": "Register"})

@app.get("/post/{post_id}", include_in_schema=False)
def post_detail(request: Request, post_id: int):
    return {"message": "Post Detail placeholder"}

@app.get("/user/{username}", include_in_schema=False)
def user_posts(request: Request, username: str):
    return {"message": "User Posts placeholder"}

