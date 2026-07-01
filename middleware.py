import time
from fastapi import Request

async def log_requests(request: Request, call_next):
    start_time = time.time()

    print("=" * 50)
    print(f"Incoming Request")
    print(f"Method : {request.method}")
    print(f"Path   : {request.url.path}")

    response = await call_next(request)

    process_time = time.time() - start_time

    print(f"Status : {response.status_code}")
    print(f"Time   : {process_time:.4f} seconds")
    print("=" * 50)

    return response