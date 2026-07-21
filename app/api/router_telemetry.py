from fastapi import APIRouter
from fastapi.responses import JSONResponse, StreamingResponse
from app.telemetry.sse_stream import telemetry_service

router = APIRouter(prefix="/telemetry", tags=["Real-Time Telemetry"])

@router.get("/stats")
async def get_stats():
    """Retrieve cumulative telemetry statistics."""
    return JSONResponse(telemetry_service.get_stats())

@router.get("/stream")
async def sse_stream():
    """Server-Sent Events (SSE) Stream for real-time UI dashboard metrics."""
    return StreamingResponse(
        telemetry_service.sse_event_generator(),
        media_type="text/event-stream"
    )
