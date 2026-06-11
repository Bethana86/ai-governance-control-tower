# Walkthrough - Gemini Enterprise Agent Control Tower

The application has been successfully updated and aligned with **Google's Gemini Enterprise Agent Platform**. It functions as an autonomous, Material-styled control tower enforcing safety thresholds, function call validation, and real-time grounding checks on Gemini model endpoints.

All codebase files are located in:
- Local Workspace: `C:/Users/ASUA/.gemini/antigravity/scratch/ai-governance-control-tower/`
- GitHub Repository: [Bethana86/ai-governance-control-tower](https://github.com/Bethana86/ai-governance-control-tower)

---

## 🎨 Google Platform Alignment Updates

1. **Material Design & Branding**:
   - Replaced all layout headers and titles with **Gemini Agent Control Tower**.
   - Integrated the official multi-colored **Google Gemini Sparkle** SVG emblem (blue, purple, red, yellow gradients) in the sidebar.
   - Refactored `style.css` variables to conform to Material Design standards, using official Google primary blue (`#1a73e8`), green (`#137333`), red (`#c5221f`), and yellow (`#b06000`) accents on standard off-white backgrounds.

2. **Gemini Agent Guardrail Suite**:
   - **Tool Parameter Lockout**: Checks parameters passed to Gemini tools, blocking destructive bash commands (e.g. `rm -rf`, `delete_database`) or service command overrides.
   - **Google Search Grounding Verifier**: Computes grounding validation metrics and displays citation check ratings (e.g. `Passed (98% Grounded)`) on LLM output streams.
   - **GCP Key Guard**: Automatically shields against the leakage of Google Cloud service account keys.

3. **Multi-Framework Compliance Auditor**:
   - Added an interactive selector row in the **Compliance Hub** tab allowing users to toggle checklists between **HIPAA**, **SOC 2 Type II**, **EU GDPR**, **India's DPDP Act (2023)**, and **Google Gemini Platform Trust standards**.
   - Dynamically re-renders regulatory checklist cards mapping technical controls to the specific audit sections of each standard.
   - Updated **Export Audit Report** to generate a complete compliance report conforming to the status of the currently selected framework, active policies, and cryptographic ledger.
   - Integrated new default policy rules: **GDPR Right to Erasure** (Articles 15/17), **DPDP Aadhaar Guard** (Aadhaar redaction), and **SOC 2 Processing Integrity** boundary guards.

---

## 🚀 How to Run and Verify the Application

The background server is running and serving the updated assets.

1. **Refresh your browser** and visit:
   [http://localhost:8080](http://localhost:8080)
2. **Interact with the Compliance Hub**:
   - Navigate to the **Compliance Hub** tab.
   - Switch between the **SOC 2 Type II**, **GDPR (EU)**, and **DPDP Act (India)** standards using the selector buttons.
   - Notice the checklist updates dynamically to present aligned controls and section numbers (e.g. Section 8(5) Aadhaar shielding under the DPDP Act).
   - Click **Verify Chain Integrity** to test the tamper-evident SHA-256 blockchain ledger.
   - Click **Export Audit Report** to download a formatted text file capturing the active standard checklist.
3. **Test the New Heuristics**:
   - Go to the **Safety & Security Playground** (or use the Policy dry-run box).
   - Enter a prompt with an Aadhaar card (e.g. `1234-5678-9012`) or ask to delete data (`delete my personal information from your logs`).
   - Run the check and observe the **DPDP Aadhaar Guard** or **GDPR Right to Erasure** policies mask the data or flag compliance in the logs.
4. **Git Synchronization**:
   - All changes have been synchronized with the remote GitHub repository.
