# Agent Policy and Compliance Tower — Enterprise Modular Repository Architecture

Enterprise-grade governance, zero-trust security guardrail, and tamper-evident audit platform for multi-agent systems built natively for the **Google AI Ecosystem (Gemini Enterprise Agent Platform)**.

---

## 📁 Modular Directory & Package Layout

```
ai-governance-control-tower/
├── app/                            # Enterprise Modular Application Package
│   ├── __init__.py
│   ├── main.py                     # Primary FastAPI application bootstrapper & factory
│   ├── core/                       # Core Configuration & Security Services
│   │   ├── config.py               # Application settings, SLA parameters & GCP key versions
│   │   └── security.py             # RSA-PSS Cryptographic signing & Cloud KMS verification
│   ├── gateway/                    # Policy Ingress & Egress Gateway Module
│   │   ├── scanner.py              # Zero-Trust Prompt Payload Scanner Service
│   │   └── patterns.py             # Compiled Regex Security Pattern Registry (Aadhaar, SSN, MRN)
│   ├── audit/                      # Cryptographic Audit Ledger Module
│   │   └── ledger.py               # SHA-256 Block Chain Manager & BigQuery DDL exporter
│   ├── telemetry/                  # Real-Time Telemetry & Observability
│   │   └── sse_stream.py           # Server-Sent Events (SSE) Stream Publisher
│   ├── agentic/                    # Fusion AI Multi-Agent System Integration
│   │   └── fusion_ai.py            # Orchestrator, TimesFM 2.0, BQML & Chatbot ReAct Engine
│   └── api/                        # Modular REST API Routers
│       ├── router_gateway.py       # POST /api/v1/gateway/scan
│       ├── router_audit.py         # GET /api/v1/audit/blocks, POST /api/v1/audit/verify
│       ├── router_telemetry.py     # GET /api/v1/telemetry/stream, GET /api/v1/telemetry/stats
│       └── router_agentic.py       # POST /api/v1/agentic/workflow, GET /api/v1/agentic/network
├── references/                     # Architecture & Specification Documents (.docx & .png)
│   ├── Agent_Policy_and_Compliance_Tower_HLD.docx   # High-Level Architecture Document
│   ├── Agent_Policy_and_Compliance_Tower_LLD.docx   # Low-Level Technical Design Document
│   ├── Agent_Policy_and_Compliance_Tower_MVP_Scope.docx # MVP Release Scope Specification
│   ├── Agent_Policy_and_Compliance_Tower_Milestone_Roadmap.docx # Release Roadmap (MVP->Pilot->Scale)
│   ├── Agent_Policy_and_Regulatory_Compliance_Specification.docx # Legal Compliance Spec
│   ├── Feature_Wise_Implementation_Plan_and_Deployment_Roadmap.docx # Feature Plan
│   ├── hld_architecture_light_theme.png             # HLD Light Theme Architecture Diagram
│   ├── lld_architecture_diagram.png                 # LLD Component Architecture Diagram
│   ├── module2_compliance_auditor.png               # Compliance Auditor Screenshot
│   └── production_realtime_system.png              # Production System Screenshot
├── static/                         # Single-Page Application (SPA) View & CSS
├── test_application.py             # Automated API & Endpoint Test Suite
├── server.py                       # Root application launcher (`uvicorn app.main:app`)
└── README.md                       # Repository Documentation
```

---

## 🚀 How to Run the Modular Server

### 1. Launch Server:
```bash
python server.py
```
The server will start at: **http://localhost:8081/**

### 2. Run Automated API Test Suite:
```bash
python test_application.py
```

### 3. Available API Endpoints:
- `POST /api/v1/gateway/scan` — Zero-Trust prompt payload scanner
- `GET /api/v1/audit/blocks` — Retrieve SHA-256 cryptographic audit chain
- `POST /api/v1/audit/verify` — Recursive block chain integrity verifier
- `GET /api/v1/telemetry/stream` — Real-time Server-Sent Events (SSE) stream
- `GET /api/v1/telemetry/stats` — Cumulative system health metrics
- `POST /api/v1/agentic/workflow` — Execute Fusion AI multi-agent workflow
- `GET /api/v1/agentic/network` — Query active GCP Workload Identity agent service accounts
