from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse
from app.agentic.fusion_ai import fusion_ai_network

router = APIRouter(prefix="/agentic", tags=["Fusion AI Agentic Network"])

@router.get("/network")
async def get_agent_network_status():
    """Returns active Fusion AI agent identities and Workload Identity status."""
    return JSONResponse({
        "gcpProjectId": fusion_ai_network.project_id,
        "agents": [
            {
                "name": "Orchestrator Agent",
                "model": "gemini-1.5-pro-002",
                "identity": fusion_ai_network.orchestrator_sa,
                "status": "ACTIVE",
                "role": "ReAct Reasoning & Context Assembly"
            },
            {
                "name": "TimesFM 2.0 Forecasting Agent",
                "model": "TimesFM 2.0 (GPU Cloud Run)",
                "identity": fusion_ai_network.timesfm_sa,
                "status": "ACTIVE",
                "role": "Zero-Shot Time-Series Foundation Model"
            },
            {
                "name": "BQML Analytics Agent",
                "model": "BigQuery ML ARIMA_PLUS",
                "identity": fusion_ai_network.bqml_sa,
                "status": "ACTIVE",
                "role": "Historical Baseline & ARIMA+ Queries"
            },
            {
                "name": "Chatbot Agent",
                "model": "gemini-1.5-flash-002",
                "identity": fusion_ai_network.chatbot_sa,
                "status": "ACTIVE",
                "role": "Low-Latency Conversational Synthesis"
            }
        ]
    })

@router.post("/workflow")
async def run_agentic_workflow(request: Request):
    """Executes full ReAct loop across Orchestrator, TimesFM 2.0, BQML, and Chatbot agents with real-time zero-trust policy enforcement."""
    try:
        body = await request.json() if request.headers.get("content-type") == "application/json" else {}
        prompt = body.get("prompt", "Analyze demand trends for customer orders")
        try:
            demand_shock = int(body.get("demandShockPct", 0))
        except (ValueError, TypeError):
            demand_shock = 0

        result = await fusion_ai_network.execute_agentic_workflow(
            user_prompt=prompt,
            demand_shock_pct=demand_shock
        )

        return JSONResponse(result)
    except Exception as e:
        import traceback
        print("AGENTIC WORKFLOW ERROR:", traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))
