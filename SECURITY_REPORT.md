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

The `test_access.py` script covers 12 main scenarios involving authentication, profile ownership, role-based access control, and URL parameter manipulation.

The tests verify that:
- Unauthenticated requests are denied.
- Users can access their own profiles but cannot access other users' profiles.
- Invalid profile access is denied.
- Ordinary users cannot access the admin dashboard.
- The admin account can access the admin dashboard.
- Adding `?role=admin` to a request does not grant admin privileges.

**Recorded test result:** 12 out of 12 main tests passed.

An additional invalid-session-cookie check returned HTTP 401, indicating that the request was treated as unauthenticated. This additional check runs separately from the 12-test main suite.
