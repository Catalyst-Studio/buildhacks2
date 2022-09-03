from datetime import timedelta

from app import maingamefile, users
from fastapi import FastAPI, Request, Response, Depends, Form, WebSocket
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.responses import RedirectResponse, HTMLResponse, PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi_login import LoginManager
from starlette import status as stss
from pathlib import Path
from json import dumps

from app.flash import flash, get_flashed_messages

class NotAuthenticatedException(Exception):
    pass

middleware = [
    Middleware(SessionMiddleware, secret_key="sajdnflkajsndkjfnaskdnfsdzcllasdfkjnlsjkdfngbsldfgbsldqwertyuiopasdfghjklzxcvbnmpolikmujnyhbtgvrfcedxwszqa")
]

app = FastAPI(middleware=middleware)
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")
secret = "sajdnflkajsndkjfnaskdnfsdzcllasdfkjnlsjkdfngbsldfgbsldqwertyuiopasdfghjklzxcvbnmpolikmujnyhbtgvrfcedxwszqa"
manager = LoginManager(secret, token_url='/auth/token', use_cookie=True, default_expiry=timedelta(hours=72))
manager.not_authenticated_exception = NotAuthenticatedException
manager.cookie_name = "auth-key-for-cc-space"
templates.env.globals['get_flashed_messages'] = get_flashed_messages

@app.exception_handler(StarletteHTTPException)
async def custom_exception_handler(request: Request, exc: StarletteHTTPException):
    return templates.TemplateResponse("error.html", {"request": request, "error": str(exc.status_code)}, status_code=exc.status_code)


@app.exception_handler(NotAuthenticatedException)
def auth_exception_handler(request: Request, exc: NotAuthenticatedException):
    """
    Redirect the user to the login page if not logged in
    """
    return RedirectResponse(url='/auth/login')


@app.get("/")
async def root():
    return "homepage"

@manager.user_loader()
async def load_user(username: str):
    user = users.get_user(f"{str(username)}")
    print(user)
    return user

@app.get("/auth/login")
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"webname": "login", "request": request})

@app.get("/auth/signup", response_class=HTMLResponse)
async def signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})


@app.post("/auth/login")
async def login(request: Request, data: OAuth2PasswordRequestForm = Depends()):
        username = data.username
        password = data.password
        user = await load_user(username)
        if not user:
            flash(request, "The Username or password you have entered is incorrect", "danger")
            print("not user")
            return templates.TemplateResponse("login.html", {"request": request})
        key = users.password(str(password), user)
        print(user["key"])
        print(key)
        if key != user["key"]:
            flash(request, "The Username or password you have entered is incorrect", "danger")
            print("incorrect password")
            return templates.TemplateResponse("login.html", {"request": request})
        access_token = manager.create_access_token(
            data={"sub": username}
        )
        resp = RedirectResponse(url="/dashboard", status_code=stss.HTTP_302_FOUND)
        manager.set_cookie(resp, access_token)
        return resp


@app.post("/auth/signup")
async def signup(request: Request, username: str = Form("username"), password: str = Form("password"), name: str = Form("name"), email: str = Form("email"), cpassword: str = Form("cpassword"), tos: str = Form("tos"), stnl: str = Form("stnl")):
    if password == cpassword:
        check = users.checkuser(username, password, email)
        if str(check) == "good":
            users.createuser(username, password, name, tos, email)
            at = manager.create_access_token(
                data={"sub": username}
            )
            resp = RedirectResponse(url="/dashboard", status_code=stss.HTTP_302_FOUND)
            manager.set_cookie(resp, at)
            return resp
        else:
            flash(request, str(check))
            return templates.TemplateResponse("signup.html", {"request": request})
    else:
        flash(request, "Passwords do not match")
        return templates.TemplateResponse("signup.html", {"request": request})




@app.get("/dashboard",)
async def dashboard(request: Request, user = Depends(manager)):
    return templates.TemplateResponse("dashboard.html", {"webname": "Dashboard", "request": request, "user": user})

@app.get("/level/{level}")
async def level(request: Request,level , user = Depends(manager)):
    code = Path(f"app/python-levels/{level}.py").read_text()
    out = code.splitlines()
    output = '\n'.join((line) for line in out)
    print(output)
    message = Path(f"app/python-levels/{level}.message").read_text()
    return templates.TemplateResponse("level.html", {"webname": f"Level {level}", "request": request, "user": user, "code": code, "message": message, "output": output})

@app.websocket(f"/level")
async def level(websocket: WebSocket):
    token = websocket.cookies.get('auth-key-for-cc-space')
    user = await manager.get_current_user(token=token)
    if user:
        await websocket.accept()
        complete = False
        while not complete:
            data = await websocket.receive_text()
            answer = maingamefile.check(level="1", code=data)
            if answer:
                send = {"type": "good", "message": "Congratulations you have beaten this level!"}
                send = dumps(send)
                print(send)
                await websocket.send_text(send)
            else:
                send = {"type": "bad", "message": "Incorrect, please try again"}
                send = dumps(send)
                print(send)
                await websocket.send_text(send)