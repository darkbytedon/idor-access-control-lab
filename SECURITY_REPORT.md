# IDOR Vulnerability: Detection, Remediation and Automated Testing

## Project Overview

- **Technology:** Python, Flask, Requests
- **Vulnerability:** Insecure Direct Object Reference (IDOR)
- **Environment:** Local training application at `http://127.0.0.1:5000`

## Objective

Demonstrate an IDOR vulnerability, implement server-side authorization, and test that users cannot access each other's profiles.

## Vulnerability Description

Insecure Direct Object Reference (IDOR) occurs when an application uses a user-controlled identifier to access an object without properly verifying that the current user is authorized to access it.

In this lab, Alice and Bob are fictional users. The application checks whether the authenticated user's ID matches the requested profile ID before returning profile information.

## Remediation

The application performs authentication and profile-ownership checks on the server before returning profile information.

- Unauthenticated requests receive **HTTP 401 Unauthorized**.
- Requests to access another user's profile receive **HTTP 403 Forbidden**.
- Authorized users can access their own profiles.

## Automated Security Tests

The `test_access.py` script tests six scenarios:

1. Unauthenticated access is denied.
2. Alice can access her own profile.
3. Alice cannot access Bob's profile.
4. Bob can access his own profile.
5. Bob cannot access Alice's profile.
6. Alice cannot access an invalid profile ID.

**Recorded test result:** Six out of six tests passed.

## Limitations

This is a small local training lab using fictional accounts. Passing these six tests does not prove that a real application is secure or that every possible access-control vulnerability has been identified.

## Future Improvements

- Test unauthorized editing and deletion.
- Add more user roles and protected resources.
- Expand automated security test coverage.
- Run tests automatically through a continuous integration workflow.
- Document additional test cases and remediation evidence.
