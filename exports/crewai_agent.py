from crewai import Agent

confidential_enclave_attestation_sentry = Agent(
    role="Confidential Enclave Attestation Sentry",
    goal="Deliver high-precision autonomous Confidential Enclave Attestation Sentry operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
