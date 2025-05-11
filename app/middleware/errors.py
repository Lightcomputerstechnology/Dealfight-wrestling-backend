# === 3. Error Handling Middleware
# File: app/middleware/errors.py

from fastapi import Request
from fastapi.responses import JSONResponse

async def not_found_handler(request: Request, exc):
    return JSONResponse(status_code=404, content={"error": "Resource not found"})

async def server_error_handler(request: Request, exc):
    return JSONResponse(status_code=500, content={"error": "Internal server error"})
