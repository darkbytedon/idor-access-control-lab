![IDOR Security Tests](https://github.com/darkbytedon/idor-access-control-lab/actions/workflows/tests.yml/badge.svg)

#IDOR Access control security lab

A hands-on cybersecurity project demonstrating Insecure Direct Object Reference (IDOR), server-side access control, and automated security testing using Python and Flask.

## Project Overview

This project simulates a web application with two fictional users, Alice and Bob. It demonstrates how weak authorization controls can allow one user to access another user's private profile.

The project implements server-side authorization checks and automated tests to verify that users can access only their own profiles.

## Skills Demonstrated

- Web application security
- IDOR vulnerability analysis
- Authentication and authorization
- Python and Flask
- Automated security testing
- HTTP status code analysis
- Security documentation and remediation
- GitHub Actions and continuous integration

## Technologies

- Python
- Flask
- Requests
- Git and GitHub
- GitHub Actions

## Project Structure

```text
idor-access-control-lab/
├── .github/
│   └── workflows/
│       └── tests.yml
├── evidence/
│   ├── ownership_check.png
│   └── test_access.png
├── app.py
├── test_access.py
├── requirements.txt
├── SECURITY_REPORT.md
├── README.md
└── .gitignore
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/darkbytedon/idor-access-control-lab.git
cd idor-access-control-lab
```

### 2. Create a virtual environment

On Windows Command Prompt:

```bat
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Set the local secret key

For Windows Command Prompt:

```bat
set FLASK_SECRET_KEY=local-lab-key-change-me
```

This key is for local practice only. Use a securely generated secret for any real deployment.

### 5. Start the application

```bash
python app.py
```

Visit http://127.0.0.1:5000 in your browser.

## Running the Security Tests

Keep the Flask application running. Open a second terminal in the project folder, activate the virtual environment, and run:

```bat
python test_access.py
```

The automated test suite checks:

1. Unauthenticated access is denied.
2. Alice can access her own profile.
3. Alice cannot access Bob's profile.
4. Bob can access his own profile.
5. Bob cannot access Alice's profile.
6. An invalid profile ID is rejected.

**Latest verified local result: 6/6 tests passed.**

## Security Remediation

The application checks the authenticated user's ID against the requested profile owner's ID on the server.

- Unauthenticated requests receive HTTP `401 Unauthorized`.
- Requests to another user's profile receive HTTP `403 Forbidden`.
- Authorized users can access their own profiles.

Authorization must be enforced server-side for every protected resource.

## Continuous Integration

GitHub Actions runs the security tests automatically when changes are pushed or a pull request is opened.

The workflow installs dependencies, starts the Flask application, and runs the automated test suite.

The workflow badge at the top of this README displays the current CI status.

## Evidence and Security Report

The `evidence/` directory contains screenshots of the authorization check and automated test results.

See [SECURITY_REPORT.md](SECURITY_REPORT.md) for the vulnerability description, remediation, test results, and project limitations.

## Scope and Disclaimer

This is an educational project using fictional accounts and local test data. Test only systems you own or have explicit permission to assess.

Passing these tests does not prove that every possible security vulnerability has been eliminated.

## Author

**DarkByteDon**

Cybersecurity learning portfolio — application security, Python, and secure web development.
