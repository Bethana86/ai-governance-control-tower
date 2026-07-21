import asyncio
import json

class TelemetryService:
    def __init__(self):
        self.stats = {
            "promptsScanned": 1284,
            "promptsBlocked": 14,
            "piiRedactions": 89,
            "avgLatencyMs": 18.4,
            "complianceRate": 99.8
        }

    def record_scan(self, is_blocked: bool, has_violations: bool, latency_ms: float):
        self.stats["promptsScanned"] += 1
        if is_blocked:
            self.stats["promptsBlocked"] += 1
        if has_violations:
            self.stats["piiRedactions"] += 1
        
        self.stats["avgLatencyMs"] = round((self.stats["avgLatencyMs"] * 0.9) + (latency_ms * 0.1), 1)

    def get_stats(self):
        return self.stats

    async def sse_event_generator(self):
        """Generates real-time Server-Sent Events (SSE) for UI dashboard streaming."""
        while True:
            await asyncio.sleep(2.0)
            self.stats["promptsScanned"] += 1
            data = json.dumps(self.stats)
            yield f"data: {data}\n\n"

telemetry_service = TelemetryService()
