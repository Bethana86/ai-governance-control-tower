# Agent Policy and Compliance Tower — Modular Repository Architecture

Enterprise-grade governance, zero-trust security guardrail, and tamper-evident audit platform for multi-agent systems built natively for the **Google AI Ecosystem (Gemini Enterprise Agent Platform)**.

---

## 📁 Modular Directory & Package Layout

```
ai-governance-control-tower/
├── app/                            # Enterprise Modular Application Package
│   ├── __init__.py
│   ├── main.py                     # Primary FastAPI application bootstrapper & factory
│   ├── core/                       # Core Configuration & Security Services
│   │   ├── __init__.py
│   │   ├── config.py               # Application settings, SLA parameters & GCP key versions
│   │   └── security.py             # RSA-PSS Cryptographic signing & Cloud KMS verification
│   ├── gateway/                    # Policy Ingress & Egress Gateway Module
│   │   ├── __init__.py
│   │   ├── scanner.py              # Zero-Trust Prompt Payload Scanner Service
│   │   └── patterns.py             # Compiled Regex Security Pattern Registry (Aadhaar, SSN, MRN)
│   ├── audit/                      # Cryptographic Audit Ledger Module
│   │   ├── __init__.py
│   │   └── ledger.py               # SHA-256 Block Chain Manager & BigQuery DDL exporter
│   ├── telemetry/                  # Real-Time Telemetry & Observability
│   │   ├── __init__.py
│   │   └── sse_stream.py           # Server-Sent Events (SSE) Stream Publisher
│   └── api/                        # REST API Router Endpoints
│       ├── __init__.py
│       ├── router_gateway.py       # POST /api/v1/gateway/scan
│       ├── router_audit.py         # GET /api/v1/audit/blocks, POST /api/v1/audit/verify
│       └── router_telemetry.py     # GET /api/v1/telemetry/stream, GET /api/v1/telemetry/stats
├── static/                         # Single-Page Application (SPA) View & Assets
├── server.py                       # Root application launcher (`uvicorn app.main:app`)
├── Agent_Policy_and_Compliance_Tower_HLD.docx   # High-Level Architecture Document
├── Agent_Policy_and_Compliance_Tower_LLD.docx   # Low-Level Technical Design Document
├── Agent_Policy_and_Compliance_Tower_MVP_Scope.docx # MVP Release Scope Specification
└── Agent_Policy_and_Compliance_Tower_Milestone_Roadmap.docx # Milestone Release Roadmap
```

---

## 🚀 How to Run the Modular Server

### 1. Launch Server:
```bash
python server.py
```
The server will start at: **http://localhost:8081/**

### 2. Available API Endpoints:
- `POST /api/v1/gateway/scan` — Zero-Trust prompt payload scanner
- `GET /api/v1/audit/blocks` — Retrieve SHA-256 cryptographic audit chain
- `POST /api/v1/audit/verify` — Recursive block chain integrity verifier
- `GET /api/v1/telemetry/stream` — Real-time Server-Sent Events (SSE) stream
- `GET /api/v1/telemetry/stats` — Cumulative system health metrics
