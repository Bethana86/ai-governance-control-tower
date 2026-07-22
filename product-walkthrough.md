# Agent Policy and Compliance Tower — Product Walkthrough

This document provides a comprehensive walk-through of the **Agent Policy and Compliance Tower** system features, user personas, operational flows, and technical stack details.

---

## 🛠️ Complete Technical Stack Architecture

The application is architected as a decoupled, real-time single-page application (SPA) powered by a high-performance Python ASGI backend and a modern vanilla client.

### 1. Backend Service Layer
* **Web Framework**: **FastAPI (ASGI)** — Used for high-concurrency, asynchronous REST routing and SSE streaming.
* **Server**: **Uvicorn** — Production-ready, lightning-fast ASGI server.
* **Security & Cryptography**:
  * **Asymmetric Signing**: RSA-PSS (2048-bit keys) with SHA-256 via Python `cryptography` package.
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

## 👥 User Personas & Operational Journeys

### 1. Security Administrator (Zero-Trust Guardrail)
* **Goal**: Monitor and configure active guardrail boundaries.
* **Journey**: Opens **Safety & Security**, loads a telemetry preset (e.g. SQL Injection attack), runs dry-run checks to verify that the Gateway intercepts the prompt immediately, and reviews the auto-remediation details in the system event modal.

### 2. Compliance Auditor (Write-Once Cryptographic Ledger)
* **Goal**: Validate that all user prompts and agent responses comply with regulatory standards.
* **Journey**: Navigates to **Compliance Hub**, switches between standard frameworks (GDPR, SOC 2, HIPAA, DPDP Act), reviews the live cryptographic audit logs, and triggers a full blockchain integrity check.

### 3. Business & Risk Analyst (Explainability & Simulations)
* **Goal**: Understand model decision parameters and simulate demand shocks.
* **Journey**: Uses **Explainability** to inspect token SHAP attribution values and runs counterfactual scenarios. Switches to **Agentic Hub**, adjusts the demand shock slider, and triggers the orchestrator agent workflow to calculate fused forecasts.

---

## 🚀 Step-by-Step Feature Walkthrough

### Step 1: Real-Time Telemetry Dashboard
1. Launch the server (`python server.py`) and visit `http://localhost:8081/?tab=dashboard`.
2. Notice the live-updating cumulative counters: **System Risk Index**, **Blocked Requests**, **Redacted Fields**, and **Compliance Alignment Rate**.
3. View the **Live Active Policy Telemetry Stream** panel. The backend streams synthetic production traffic via SSE. Intercept logs appear line-by-line with millisecond-accurate timestamps.

### Step 2: Safety & Security Guardrails
1. Select the **Safety & Security** tab.
2. Under **Telemetry Ingress Simulation Presets**, click **PII Leakage Attempt** or **SQL Injection**. The input simulator field will immediately fill with a malicious prompt string.
3. Click **Run Gateway Scan**. The UI displays the scan result:
   * **Clean prompt**: Green "CLEAN" status.
   * **Malicious prompt**: Red "BLOCKED" status showing the matched policy rules (e.g., `SQL-INJECTION-01` or `HIPAA-01`).
4. Look at the **Google Safety Settings Integration** gauge. Drag any slider (Hate Speech, Harassment) to observe the active guard factor dial transition between SECURE, WARN, and RISKY.

### Step 3: Policy Engine Customization
1. Navigate to the **Policy Engine** tab.
2. You will see a list of pre-configured policies (e.g., `HIPAA-PHI-REDACTION`, `SOC2-INTEGRITY`). Toggle any switch to enable or disable the policy rule instantly in-memory.
3. Test custom regular expressions using the **Interactive Policy Sandbox**. Type a custom regex in the pattern field (e.g., `\b[0-9]{4}-[0-9]{4}\b`), enter some test text in the simulator box, and watch matches get flagged in real time.

### Step 4: Compliance Center & Tamper-Evident Ledger
1. Select the **Compliance Hub** tab.
2. Switch between **HIPAA**, **SOC 2**, **GDPR**, **DPDP Act (India)**, and **Gemini Trust**. Notice the compliance requirements checklist updating dynamically according to the selected standard.
3. View the black terminal labeled **Cryptographic Write-Once Audit Logs**. Every action you took (switching tabs, scanning prompts, modifying policies) is recorded here as a block.
4. Click **Verify Chain Integrity**. A progress loader will run, followed by a popup confirming cryptographic chain integrity. The status badge will update to **VERIFIED SECURE**.
5. Click **Export Audit Report** to download a `.txt` audit ledger file containing all configuration rules and cryptographic log hashes.

### Step 5: Model Explainability (SHAP & Counterfactuals)
1. Go to the **Explainability** tab.
2. View the **Token-Level Attribution** heatmap. Green indicates words contributing to a "safe" model rating; red shows words that trigger policy violations.
3. Use the **Counterfactual Risk Modeler** sliders (Age, Diastolic BP, HbA1c, Admissions) to adjust patient parameters. The gauge dial updates dynamically to show how risk probability values change based on patient demographic shifts.

### Step 6: Multi-Agent Orchestration Hub
1. Click the **Agentic Hub** tab.
2. Review the **Agent Network Registry** showing active Workload Identity Service Accounts mapped to specific models (`gemini-1.5-flash`, etc.).
3. Choose a dataset context (e.g., Retail Sales) and set the simulated shock factor using the range slider.
4. Click **Trigger Agentic Run**. The inter-agent terminal streams the interaction flow step-by-step (e.g., Orchestrator -> BQML -> TimesFM), and displays the final fused ensembled forecasts.
