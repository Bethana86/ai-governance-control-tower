# Agentic Intelligence Hub & Compliance Control Tower

Agentic Intelligence Hub (Fusion AI): Designed an autonomous GCP-based agentic ecosystem integrating Gemini (Vertex AI), TimesFM, and Google ADK for multi-step reasoning and time-series forecasting; engineered containerized microservices on Cloud Run and BigQuery / BigQuery ML managed via GitHub, with full AgentOps, MLflow, OTEL, and Cloud Monitoring observability.

---

## 🛠️ Technology Stack & Role Assignments

Below is the complete engineering matrix of the Governance Control Plane and the Forecasting Ecosystem:

| Layer | Component | Technology / Stack | Purpose & Responsibility |
| :--- | :--- | :--- | :--- |
| **Control Plane** | **User Interface (UI)** | HTML5 & Vanilla CSS3 | Sleek responsive dark-theme glassmorphism with dynamic status alerts. |
| **Control Plane** | **Front Logic** | Vanilla ES6 JavaScript | DOM updates, SSE real-time stream subscription, Web Cryptography verifications. |
| **Control Plane** | **Verifications** | Web Cryptography API | Strict browser-native cryptographic hashing (`crypto.subtle.digest`) with standard context fallbacks. |
| **Control Plane** | **Visualizer** | Chart.js | Horizontal bar rendering of token SHAP features and risk gauges. |
| **Control Plane** | **Web Framework** | FastAPI (Python) | Direct async routing, SSE streaming, and microservice validation APIs. |
| **Control Plane** | **Zero-Trust Scanner** | Regex Scanner Service | Custom modular expression matcher scanning for SSN, PII, SQL, and tool bypasses. |
| **Control Plane** | **Ledger Database** | BigQuery & Local memory | Cryptographically linked write-once SHA-256 logs with sequential queue execution. |
| **Control Plane** | **Envelope Security** | Cloud KMS & Cryptography | RSA-PSS (2048-bit keys) with SHA-256 for signing compliance blocks. |
| **Workload App** | **Orchestrator** | Google Antigravity SDK | Coordinates the autonomous agent reasoning, tool bindings, and state lifecycle. |
| **Workload App** | **Reasoning Core** | Gemini 1.5 Pro | Multi-turn reasoning agent resolving patterns and drafting analyst briefings. |
| **Workload App** | **Statistical Forecast**| BigQuery ML | Trains and queries native BQML ARIMA+ models and KMeans anomaly detection. |
| **Workload App** | **Deep Learning** | Google TimesFM Engine | Standalone zero-shot Transformer forecasting engine generating continuous quantiles. |
| **Workload App** | **Observability** | MLflow / AgentOps / OTEL | Logs run configurations, parameters, and forecast metrics (RMSE, MAPE). |

---

## 🏗️ System Architecture Diagram

```mermaid
graph TD
    %% Styling definitions
    classDef client fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#f8fafc;
    classDef orchestrator fill:#1e1b4b,stroke:#818cf8,stroke-width:2px,color:#f8fafc;
    classDef engine fill:#022c22,stroke:#34d399,stroke-width:2px,color:#f8fafc;
    classDef governance fill:#701a75,stroke:#f472b6,stroke-width:2px,color:#f8fafc;
    classDef infrastructure fill:#451a03,stroke:#fb923c,stroke-width:2px,color:#f8fafc;

    %% Nodes
    subgraph ClientLayer ["Control Tower Interface Layer"]
        UI["Glassmorphic UI <br> (Dashboard Canvas)"]:::client
        API["FastAPI Control Web Server <br> (server.py)"]:::client
    end

    subgraph AgentLayer ["Agentic Orchestration Layer"]
        ADK["google-antigravity Agent <br> (agent.py)"]:::orchestrator
    end

    subgraph ForecastLayer ["Dual-Mode Forecasting & Analytical Engines"]
        BQML["BigQuery ML Engine"]:::engine
        TimesFM["TimesFM Zero-Shot Engine"]:::engine
        Fusion["Ensemble Fusion Engine"]:::engine
    end

    subgraph GovLayer ["AgentOps & Telemetry Governance Control Plane"]
        MLflow["MLflow Registry"]:::governance
        Monitoring["Cloud Monitoring Logs"]:::governance
        Gateway["Zero-Trust Policy Gateway <br> (/api/v1/gateway/scan)"]:::governance
        Ledger["Tamper-Evident Ledger <br> (/api/v1/audit/blocks)"]:::governance
    end

    %% Flows
    UI <-->|SSE Stream & REST API| API
    API <-->|Execute Pipeline| ADK
    
    ADK -->|Invoke Tools| BQML
    ADK -->|Invoke Tools| TimesFM
    
    BQML -->|Live GCP BQML ARIMA+ / KMeans| GCP_BigQuery[("GCP BigQuery")]:::infrastructure
    
    TimesFM -->|Live Zero-Shot Transformer| GCP_Vertex[("GCP Vertex AI")]:::infrastructure

    BQML -->|Historical & Model Metrics| Fusion
    TimesFM -->|Zero-Shot Forecasts & Quantiles| Fusion
    
    Fusion -->|Variance-Weighted Fusion| ADK
    
    ADK -->|Log Experiment Telemetry| MLflow
    ADK -->|Emit Audit Telemetry| Monitoring
    
    %% Intercept Flow
    ADK & BQML & TimesFM -.->|Scan Prompt & Log Action| Gateway
    Gateway -->|Append Verified Block| Ledger
    
    class UI,API client;
    class ADK orchestrator;
    class BQML,TimesFM,Fusion engine;
    class MLflow,Monitoring,Gateway,Ledger governance;
    class GCP_BigQuery,GCP_Vertex infrastructure;
```
