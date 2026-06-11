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

3. **Gemini API Safety Configurator (Explainability)**:
   - Added a new panel tab called **Gemini Harm Settings**.
   - Integrates sliders representing Gemini API's official content block threshold categories: *Harassment*, *Hate Speech*, *Sexually Explicit*, and *Dangerous Content*.
   - Adjusting thresholds dynamically shifts the **Active Guard Factor** dial (Secure, Warn, Risky) and updates simulated policy logs.

---

## 🚀 How to Run the Application

The background server task has restarted in the background and is serving the updated assets.

1. **Refresh your browser** and visit:
   [http://localhost:8080](http://localhost:8080)
2. **Interact with the New Features**:
   - **Dashboard**: Run **Simulate Stream** to see the logs showing `gemini-1.5-pro` and `gemini-1.5-flash` running with Google Search Grounding verification indexes.
   - **Sandbox Playground**: Select the **Malicious Tool Call** preset and click **Execute Safety Shield** to see Gemini's tool validation block parameter execution in action.
   - **Explainability**: Select the new **Gemini Harm Settings** tab. Move the sliders to toggle safety thresholds between *Block None* and *Block Most* to watch the guard dial calculate real-time safety scores.
