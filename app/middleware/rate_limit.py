# === 6. Rate Limiting Middleware (app/middleware/rate_limit.py) ===

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from fastapi.responses import JSONResponse
import time

class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, delay_seconds=1):
        super().__init__(app)
        self.delay = delay_seconds
        self.clients = {}

    async def dispatch(self, request: Request, call_next):
        ip = request.client.host
        now = time.time()
        last = self.clients.get(ip, 0)
        if now - last < self.delay:
            return JSONResponse({"detail": "Too many requests"}, status_code=429)
        self.clients[ip] = now
        return await call_next(request)
