# TCS ACT - Production Transition Blueprint

This document outlines the multi-phase engineering plan required to transition the **TCS ACT - Agent Control Tower** from a high-fidelity simulator prototype into a real-time, production-grade enterprise middleware gateway.

---

## 🏗️ 1. Architecture: The Middleware Gateway Proxy

In production, all safety checks, policies, and redactions must execute on a server-side gateway proxy positioned between your client applications and Google's Gemini API endpoints.

```
[Client Application] 
       │ (Prompt payload)
       ▼
┌────────────────────────────────────────────────────────┐
│  TCS ACT Middleware Gateway (FastAPI / Go)            │
│  1. Ingress Shield (Jailbreak, PII Redaction)          │
│  2. Policy Engine Validation                           │
└────────────────────────────────────────────────────────┘
       │ (Sanitized prompt)
       ▼
[Google Gemini API / Vertex AI]
       │ (Raw model response + Grounding Metadata)
       ▼
┌────────────────────────────────────────────────────────┐
│  TCS ACT Egress Shield                                 │
│  1. Output Verification (Tool parameters, secret keys) │
│  2. SHA-256 Block Generation & Ledger Logging          │
└────────────────────────────────────────────────────────┘
       │ (Secure, grounded response)
       ▼
[Client Application]
```

### Key Technical Specifications:
* **Technology Stack**: Python (FastAPI) or Go (Gin) to maintain a latency overhead under 25ms.
* **Scale & Hosting**: Deploy as a containerized service (Docker) on **Google Kubernetes Engine (GKE)** or **Cloud Run** with auto-scaling policies to handle spikes in request volumes.
* **Caching**: Integrate an in-memory **Redis** cache to store safety-cleared answers for common query patterns, reducing overall Gemini token costs.

---

## 🔒 2. Security: Enterprise Guardrail Upgrades

Replace the client-side regex rules with robust, machine-learning-driven guardrail services:

* **PII/PHI Masking (GDPR / HIPAA / DPDP)**:
  * Deploy **Microsoft Presidio** or integrate **Google Cloud DLP (Data Loss Prevention) API** as a dedicated microservice.
  * Implement named-entity recognition (NER) models to dynamically detect and redact complex entities, including Indian Aadhaar cards, medical record numbers (MRNs), and context-specific demographic profiles.
* **Jailbreak & Prompt Injection Defense**:
  * Implement semantic scanning layer libraries like **LLM-Guard** or **Nvidia NeMo Guardrails**.
  * Use a lightweight binary classification model to score incoming prompts for adversarial intent before passing payload data downstream.
* **Secure Tool parameter Validation**:
  * Enforce strict JSON schema validation for all parameters outputted to tool-calls by Gemini, automatically neutralizing system command injections (e.g. `rm -rf`, shell characters, database commands).

---

## ⚡ 3. Gemini Platform Native Integration

Replace simulated endpoints with official SDK and API pipelines:

* **Safety settings Mapping**:
  * Bind the dashboard UI threshold sliders directly to Vertex AI’s native `HarmCategory` and `HarmBlockThreshold` configurations:
    * `HARM_CATEGORY_HARASSMENT`
    * `HARM_CATEGORY_HATE_SPEECH`
    * `HARM_CATEGORY_SEXUALLY_EXPLICIT`
    * `HARM_CATEGORY_DANGEROUS_CONTENT`
  * Intercept block responses (`finishReason: SAFETY`) and map them directly to security alert triggers in the dashboard interface.
* **Google Search Grounding**:
  * Enable the native Google Search tool parameter in the Vertex AI SDK (`googleSearchRetrieval`).
  * Extract grounding citation attributes from `groundingMetadata.webSearchQueries` and evaluate citation precision scores dynamically.

---

## 📜 4. Ledger: Immutable Cryptographic Auditing

Transition the temporary in-memory ledger list to a secure, write-once ledger:

* **Ledger Database**:
  * Write transaction records to **AWS QLDB**, **Google Cloud Blockchain Node Engine**, or a secure SQL database configured with append-only ledger tables (e.g. PostgreSQL with schema auditing constraints).
* **Cryptographic Signatures**:
  * Utilize **Google Cloud KMS (Key Management Service)** to sign each ledger block. The SHA-256 links will lock each log entry to the hash of the preceding record, guaranteeing complete, tamper-proof audit histories for SOC 2 Type II evaluations.

---

## 📊 5. Observability & Observability Telemetry

Move the dashboard visuals into standard telemetry formats:

* **OpenTelemetry Instrumentation**:
  * Trace all prompt flows using OpenTelemetry standards, generating metrics on request latency, token consumption, policy block rates, and grounding scores.
* **Telemetry Collectors**:
  * Route metrics to enterprise aggregation systems like **Datadog**, **New Relic**, or **Prometheus/Grafana**.
* **Dashboard Data API**:
  * Build a secure backend API that query audits and metrics from the database, allowing the control tower dashboard to render live telemetry instead of mock loop generators.

---

## 🔑 6. IAM & Enterprise Controls

* **OAuth 2.0 / OIDC Integration**:
  * Implement authentication on the Control Tower console using **Google Workspace SSO**, **Okta**, or **Azure Active Directory**.
* **Role-Based Access Control (RBAC)**:
  * Configure three distinct profiles:
    * **SecOps Admin**: Access to deploy and toggle active policy rules and threshold parameters.
    * **Auditor**: Access to view historical ledger verifications and download signed PDF/CSV compliance reports.
    * **AI Developer**: Access to sandboxed prompt dry-run playground.
