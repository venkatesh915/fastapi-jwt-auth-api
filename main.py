from fastapi import FastAPI
from database import Base, engine
from middleware import log_requests



from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler

from routers import auth_router, user_router, admin_router
from limiter import limiter   

app = FastAPI(title="JWT OTP Role Based API")

app.middleware("http")(log_requests)

app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

app.add_exception_handler(
    RateLimitExceeded,
    _rate_limit_exceeded_handler
)

Base.metadata.create_all(bind=engine)

app.include_router(auth_router.router)
app.include_router(user_router.router)
app.include_router(admin_router.router)


@app.get("/")
def home():
    return {"message": "API running"}