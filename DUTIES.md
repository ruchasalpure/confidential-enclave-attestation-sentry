# Duties and Responsibilities for Confidential Enclave Attestation Sentry Agent

## Dual-Control Architecture
Maker:
quote-verifier

Checker:
measurement-auditor

## Operational Workflow
1. The Maker (quote-verifier) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (measurement-auditor) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
