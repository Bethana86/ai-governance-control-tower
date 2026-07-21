import re

# Compiled Regex Patterns for Zero-Trust Ingress Security
PATTERNS = {
    "AADHAAR": re.compile(r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}\b'),
    "SSN": re.compile(r'\b\d{3}-\d{2}-\d{4}\b'),
    "MRN": re.compile(r'\bMRN-\d{6}\b', re.IGNORECASE),
    "PROMPT_INJECTION": re.compile(
        r'(ignore previous instructions|system prompt override|bypass guardrails|jailbreak|developer mode)',
        re.IGNORECASE
    ),
    "DESTRUCTIVE_TOOL": re.compile(
        r'(rm\s+-rf|drop\s+table|delete\s+from|format\s+c:|execute_bash)',
        re.IGNORECASE
    )
}
