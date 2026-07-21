import time
import hashlib
from app.gateway.patterns import PATTERNS

class ZeroTrustScanner:
    def __init__(self):
        pass

    def evaluate_prompt(self, prompt: str):
        """Scans prompt payload for PII entities, prompt injection, and tool lockout violations."""
        start_time = time.time()
        redacted_prompt = prompt
        detected_violations = []

        # 1. Aadhaar Redaction (India DPDP Act 2023)
        if PATTERNS["AADHAAR"].search(prompt):
            redacted_prompt = PATTERNS["AADHAAR"].sub("****-****-1234 [AADHAAR MASKED]", redacted_prompt)
            detected_violations.append("India DPDP Act 2023 Sec. 8 (Aadhaar Pattern)")

        # 2. SSN Redaction (HIPAA §164.312)
        if PATTERNS["SSN"].search(prompt):
            redacted_prompt = PATTERNS["SSN"].sub("***-**-6789 [SSN MASKED]", redacted_prompt)
            detected_violations.append("HIPAA §164.312(a)(1) Access Control (SSN Pattern)")

        # 3. Medical Record Number Redaction (HIPAA Safe Harbor)
        if PATTERNS["MRN"].search(prompt):
            redacted_prompt = PATTERNS["MRN"].sub("MRN-****** [MRN MASKED]", redacted_prompt)
            detected_violations.append("HIPAA Medical Record Masking (MRN)")

        # 4. Prompt Injection & Jailbreak Check
        is_blocked = False
        if PATTERNS["PROMPT_INJECTION"].search(prompt):
            is_blocked = True
            detected_violations.append("Gemini Safety Guardrails: Prompt Injection Detected")

        # 5. Destructive Tool Lockout Check
        if PATTERNS["DESTRUCTIVE_TOOL"].search(prompt):
            is_blocked = True
            detected_violations.append("Tool Parameter Lockout: Destructive Execution Command Blocked")

        elapsed_ms = round((time.time() - start_time) * 1000, 2)
        prompt_hash = hashlib.sha256(redacted_prompt.encode('utf-8')).hexdigest()

        return {
            "status": "BLOCKED" if is_blocked else "ALLOWED",
            "originalPrompt": prompt,
            "redactedPrompt": redacted_prompt,
            "violations": detected_violations,
            "latencyMs": elapsed_ms,
            "promptHash": prompt_hash
        }

scanner_service = ZeroTrustScanner()
