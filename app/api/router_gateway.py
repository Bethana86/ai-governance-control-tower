from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from app.gateway.scanner import scanner_service
from app.audit.ledger import ledger_service
from app.telemetry.sse_stream import telemetry_service

router = APIRouter(prefix="/gateway", tags=["Policy Gateway"])

@router.post("/scan")
async def scan_prompt(request: Request):
    """Synchronous Ingress Zero-Trust Prompt Scanner Endpoint."""
    try:
        body = await request.json()
        prompt = body.get("prompt", "")
        agent_id = body.get("agentId", "sa:fusion-ai-orchestrator@gcp-project.iam")

        scan_result = scanner_service.evaluate_prompt(prompt)

        # Update telemetry metrics
        telemetry_service.record_scan(
            is_blocked=(scan_result["status"] == "BLOCKED"),
            has_violations=(len(scan_result["violations"]) > 0),
            latency_ms=scan_result["latencyMs"]
        )

        # Append to Cryptographic Audit Ledger
        new_block = ledger_service.add_block(
            agent_id=agent_id,
            prompt_digest=scan_result["promptHash"],
            violations=scan_result["violations"]
        )

        scan_result["blockId"] = new_block["blockId"]
        scan_result["kmsSignature"] = new_block["kmsSignature"]

        return JSONResponse(scan_result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
