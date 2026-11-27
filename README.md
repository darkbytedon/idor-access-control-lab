# IDOR Access Control Security Lab

![IDOR Security Tests](https://github.com/darkbytedon/idor-access-control-lab/actions/workflows/tests.yml/badge.svg)

A practical application-security portfolio project demonstrating Insecure Direct Object Reference (IDOR), Broken Object Level Authorization (BOLA), server-side authorization and automated security testing using Python and Flask.

## Project Overview

This repository contains an original Flask access-control lab and a separate controlled before-and-after IDOR demonstration.

The project demonstrates how missing object-level authorization can allow one authenticated user to access another user's private information, and how server-side ownership checks prevent unauthorized access.

## Project Highlights

- Investigated object-level authorization.
- Created a controlled IDOR vulnerability demonstration.
- Reproduced unauthorized cross-user profile access.
- Implemented server-side ownership validation.
- Performed manual and automated retesting.
- Integrated GitHub Actions for continuous testing.
- Documented the assessment in a professional security report.

## Project Structure

- `app.py` — Original Flask training application.
- `test_access.py` — Original integration security tests.
- `vulnerable-demo/` — Intentionally vulnerable local demonstration.
- `remediated-demo/` — Corrected implementation.
- `test_assessment.py` — Automated before-and-after tests.
- `SECURITY_REPORT.md` — Professional IDOR security assessment.
- `evidence/` — Test output and supporting screenshots.
- `.github/workflows/tests.yml` — GitHub Actions workflow.

## Technologies

- Python
- Flask
- Requests
- Python unittest
- Git and GitHub
- GitHub Actions
- Linux / Ubuntu

## Automated Testing

The project contains two separate test suites.

### Original integration tests

Run the original Flask application with a local secret key, then execute `python test_access.py`.

The 13 checks cover authentication, profile ownership, administrative access, URL parameter manipulation and invalid session cookies.

### Before-and-after IDOR assessment

Run:

`python -m unittest -v test_assessment.py`

This suite contains:

- 4 tests confirming the expected behaviour of the intentionally vulnerable application.
- 6 tests verifying the corrected application's authorization controls.

Recorded local result: 10 out of 10 tests passed.

The vulnerable tests passing means the deliberately insecure behaviour was reproduced successfully. It does not mean the vulnerable application is secure.

### Combined testing

GitHub Actions is configured to run both suites on pushes, pull requests and manual workflow dispatches.

## Security Assessment

See [SECURITY_REPORT.md](SECURITY_REPORT.md) for the complete assessment, including:

- Executive summary and scope.
- Vulnerability reproduction.
- Root cause analysis.
- Demonstrated and potential security impact.
- Server-side remediation.
- Manual and automated retesting.
- Assessment limitations and evidence integrity.

## Important Security Notice

The applications use fictional accounts and local training data.

The intentionally vulnerable demonstration must remain restricted to `127.0.0.1` and must never be deployed publicly.

The training login mechanism is simplified and is not suitable for production authentication.

The original published application history already contained an ownership check. The vulnerable demonstration was created separately for controlled educational testing.

## Disclaimer

This is an educational cybersecurity portfolio project, not a report of a real client engagement or production penetration test.

Test only systems you own or have explicit permission to assess.

## Author

**DarkByteDon**

Cybersecurity learning portfolio — application security, Python and secure web development.
