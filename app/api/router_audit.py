from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.audit.ledger import ledger_service

router = APIRouter(prefix="/audit", tags=["Cryptographic Audit Ledger"])

@router.get("/blocks")
async def get_audit_blocks():
    """Retrieve historical audit ledger blocks."""
    return JSONResponse({"blocks": ledger_service.get_all_blocks()})

@router.post("/verify")
async def verify_audit_chain():
    """Executes recursive SHA-256 prevHash chain verification."""
    return JSONResponse(ledger_service.verify_integrity())
