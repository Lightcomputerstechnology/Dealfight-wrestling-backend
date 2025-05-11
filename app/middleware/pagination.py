from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

class PaginationMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            page = int(request.query_params.get("page", 1))
            limit = int(request.query_params.get("limit", 10))
        except ValueError:
            page = 1
            limit = 10

        # Ensure valid bounds
        page = max(page, 1)
        limit = min(max(limit, 1), 100)  # limit between 1–100

        # Inject into request state
        request.state.page = page
        request.state.limit = limit

        response = await call_next(request)
        return response