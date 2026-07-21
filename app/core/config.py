import os

class Settings:
    PROJECT_NAME: str = "Agent Policy & Regulatory Compliance Engine"
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"
    PORT: int = 8081
    HOST: str = "0.0.0.0"
    SLA_LATENCY_MAX_MS: float = 25.0
    GCP_PROJECT_ID: str = os.getenv("GCP_PROJECT_ID", "gcp-project")
    KMS_KEY_VERSION: str = os.getenv(
        "KMS_KEY_VERSION",
        "projects/gcp-project/locations/global/keyRings/governance-ring/cryptoKeys/audit-signer/cryptoKeyVersions/1"
    )

settings = Settings()
