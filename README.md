# Secure CI/CD Pipelines

A reusable GitHub Actions security gate, two custom Semgrep rules with tests, and a guide to
testing for IDOR.

## Contents

| Path | What it is |
|---|---|
| `.github/workflows/security-gate.yml` | Reusable workflow. Runs Semgrep (`p/security-audit`) and Gitleaks. Fails the build on findings |
| `rules/semgrep-custom-rules.yml` | `python-hardcoded-jwt-secret` (weak literal secret passed to `jwt.encode`, in positional, `key=` and `secret_key=` form) and `insecure-md5-usage` |
| `rules/semgrep-custom-rules.py` | Test cases for those rules. Run `semgrep --test rules/` |
| `docs/IDOR_Testing_Methodology.md` | Checklist and method for finding Insecure Direct Object References |

## Use the gate in another repository

```yaml
jobs:
  security:
    uses: Chetan-Biranje/Secure-CI-CD-pipelines/.github/workflows/security-gate.yml@main
```

## Use the custom rules

```bash
semgrep scan --config rules/semgrep-custom-rules.yml path/to/code
```
