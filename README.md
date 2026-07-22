# Agent Policy and Compliance Tower — Enterprise Modular Repository Architecture

Enterprise-grade governance, zero-trust security guardrail, and tamper-evident audit platform for multi-agent systems built natively for the **Google AI Ecosystem (Gemini Enterprise Agent Platform)**.

---

## 🛠️ Complete Technical Stack Details

### 1. Backend Service Layer
* **Application Framework**: **FastAPI (Python)** — Handles async REST routing, Server-Sent Events (SSE) streaming, and high-concurrency requests.
* **Server Launcher**: **Uvicorn** — Production ASGI server.
* **Security & Cryptography**:
  * **Asymmetric Key Signing**: RSA-PSS (2048-bit keys) with SHA-256 via Python `cryptography` package.
  * **Key Management**: **Google Cloud KMS** — Native envelope key signing and decryption verification.
* **Ledger Database**: **Google Cloud BigQuery** — Cryptographically anchored audit blocks streamed to append-only tables.
* **Model Orchestration**: **Google GenAI SDK** — Interfaces with Google Gemini 1.5 models for policy grounding checks.
* **Analytics**: **TimesFM 2.0 (Zero-Shot Time-Series Forecast)** — Integrated into the agentic workflow ensembler.

### 2. Frontend Interface Layer
* **Structure**: **Semantic HTML5** — Lightweight, clean DOM structure with strict accessibility IDs.
* **Styling**: **Vanilla CSS3** — Curated dark-theme color palette using CSS Custom Properties (Variables), custom scrollbars, glowing indicator animations, and glassmorphic panels.
* **Logic**: **Vanilla ES6+ JavaScript** — Lightweight client engine. Features:
  * **Server-Sent Events (SSE)**: Native `EventSource` connection for real-time telemetry stream parsing.
  * **Web Cryptography API**: Browser-native cryptographic hashing (`crypto.subtle.digest`) with a strict fallback hash generator for non-secure contexts.
  * **Serialized Promise Queue**: strict FIFO promise chain to eliminate asynchronous blockchain race conditions.
  * **Visualizations**: **Chart.js (v4.x)** — Responsive Canvas-based rendering of historical policy trends.

---

## 📁 Modular Directory & Package Layout

```
ai-governance-control-tower/
|
├── app/                            # Enterprise Modular Application Package
│   ├── __init__.py
│   ├── main.py                     # Primary FastAPI application bootstrapper & factory
│   ├── core/                       # Core Configuration & Security Services
│   │   ├── config.py               # Application settings, GCP key versions & project configs
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
│
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
│
├── static/                         # Single-Page Application (SPA) View & CSS
├── test_application.py             # Automated API & Endpoint Test Suite
├── server.py                       # Root application launcher (`uvicorn app.main:app`)
├── product-walkthrough.md          # Comprehensive Guide to User Persona Journeys & Features
├── requirements.txt                # Python package dependency list
└── README.md                       # Repository Documentation
```

---

## 🚀 How to Run the Modular Server

### 1. Install Dependencies:
```bash
pip install -r requirements.txt
```

### 2. Launch Server:
```bash
python server.py
```
The server will start at: **http://localhost:8081/**

### 3. Run Automated API Test Suite:
```bash
python test_application.py
```

---

## 🌐 Available API Endpoints

* `POST /api/v1/gateway/scan` — Zero-Trust prompt payload scanner
* `GET /api/v1/audit/blocks` — Retrieve SHA-256 cryptographic audit chain
* `POST /api/v1/audit/verify` — Recursive block chain integrity verifier
* `GET /api/v1/telemetry/stream` — Real-time Server-Sent Events (SSE) stream
* `GET /api/v1/telemetry/stats` — Cumulative system health metrics
* `POST /api/v1/agentic/workflow` — Execute Fusion AI multi-agent workflow
* `GET /api/v1/agentic/network` — Query active GCP Workload Identity agent service accounts
