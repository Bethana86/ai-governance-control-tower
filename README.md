# AI Governance Control Tower

An enterprise-grade autonomous control tower for AI Governance, safety, explainability, and regulatory compliance. Tailored for regulatory-critical environments, this single-page dashboard manages and audits LLM pipelines in real time for **HIPAA**, **SOC 2 Type II**, **EU GDPR**, **India's DPDP Act (2023)**, and **Google Gemini Platform Trust standards**.

---

## 🚀 Key Features

### 1. Control Tower Dashboard (Real-Time Stream)
* **Live Telemetry Stream**: Simulates incoming LLM requests showing latency, triggered policies, processing time, and cryptographic hashes.
* **Key Risk Metrics**: Tracks overall risk index, prompt injections blocked, sensitive data fields redacted, and policy compliance rates.

### 2. Safety & Security Playground
* **Prompt Injection Shield**: Regex-based heuristic detector mapping instruction overrides, jailbreak strings, and bypass attempts.
* **Sensitive Data Masking**: Automatically detects and redacts HIPAA Safe Harbor identifiers (SSNs, emails, phone numbers, MRNs) in real time.
* **Output Validation**: Validates generated model outputs against system leakage policies (e.g., preventing raw SQL dumps or private IP addresses from reaching clients).

### 3. Governance Policy Engine
* **Rule Designer**: Form-based builder to deploy and evaluate custom regex policies (High, Medium, Info severities).
* **Dry-Run Sandbox**: Interactive textarea checking custom prompt inputs against active rules immediately.

### 4. Explainability & Model Interpretability
* **SHAP Token Attribution**: Color-coded visualization showing token-level risk contribution for tabular classification models.
* **Counterfactual Explorer**: Sliders adjusting clinical parameters (Age, BP, HbA1c, prior admissions) showing real-time alterations in readmission risk alongside explanatory suggestions.

### 5. Regulatory & Platform Compliance Hub
* **Multi-Framework Auditor**: Toggle checklists between global standards including **HIPAA (US)**, **SOC 2 Type II**, **GDPR (EU)**, **DPDP Act (India)**, and **Google Gemini Platform Trust standards**.
* **Tamper-Evident Ledger**: Write-once, append-only logs linked cryptographically using SHA-256 hashes generated through the native Web Crypto API.
* **Audit Chain Verification**: Self-audit loop calculating and verifying the integrity of the log chain to ensure zero retrospective tampering.

### 6. Multi-Agent Orchestration & Telemetry (Agentic Hub)
* **Agent Network Registry**: Real-time status cards mapping agent identities (GCP service accounts), model types, and bound tools (e.g. TimesFM zero-shot forecasting tool).
* **Interagent Event Interceptor**: Logs all message transmissions and API requests, verifying tool boundaries under SOC 2 and security policies.
* **What-If Scenario Shock Simulator**: Interactive slider triggering cooperative ensembled runs with custom demand/load shocks, logging calculations to the audit ledger.

---

## 🛠️ Project Structure

```
ai-governance-control-tower/
├── index.html        # App interface structure and semantic elements
├── style.css         # Glassmorphic light-theme styling system (navy/cyan accents)
├── app.js            # Frontend logic, simulators, security engines, and cryptography
└── requirements.txt  # Project dependency outline
```

---

## 💻 Local Setup & Execution

Since the project is built on vanilla web standards (HTML5/CSS3/ES6), it requires **zero external installations** or dependencies.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Bethana86/ai-governance-control-tower.git
   cd ai-governance-control-tower
   ```
2. **Start a local development server**:
   * *Using Python 3*:
     ```bash
     py -m http.server 8080
     ```
   * *Using Node.js* (if installed):
     ```bash
     npx http-server -p 8080
     ```
3. **Open the browser**:
   Navigate to [http://localhost:8080](http://localhost:8080) to access the dashboard.
