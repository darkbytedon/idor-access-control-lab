# IDOR Vulnerability: Detection, Remediation and Automated Testing

## Project Overview

- **Technology:** Python, Flask
- **Vulnerability:** Insecure Direct Object Reference (IDOR)
- **Environment:** Local training application at `http://127.0.0.1:5000`

## Objective

Demonstrate an IDOR vulnerability, implement server-side authorization, and test that users cannot access each other's profiles.

## Vulnerability Description

Insecure Direct Object Reference (IDOR) occurs when an application uses a user-controlled object identifier without properly verifying whether the requesting user has permission to access that object.

In this lab, Alice and Bob are fictional users. The initial vulnerable implementation allowed a user to access another user's profile by changing the profile ID in the URL.

For example, a user signed in as Alice could attempt to access `/profile/2`, which refers to Bob's profile.

## Security Impact

In a real application, this type of weakness could expose private user information or allow unauthorized actions. The impact depends on the sensitivity of the affected resource and the operations available.

## Remediation

The application now checks authentication and profile ownership on the server before returning profile information.

```python
if logged_in_user_id != user_id:
    return "Forbidden: you cannot access this profile.", 403
```

Requests to view another user's profile are rejected with HTTP `403 Forbidden`.

The Flask secret key is also loaded from the `FLASK_SECRET_KEY` environment variable rather than being hardcoded in the source code.

## Automated Tests

The `test_access.py` script tests six scenarios:

1. Unauthenticated access is denied.
2. Alice can access her own profile.
3. Alice cannot access Bob's profile.
4. Bob can access his own profile.
5. Bob cannot access Alice's profile.
6. Alice cannot access an invalid profile ID.

### Recorded Test Results

| Test case | Expected HTTP status | Result |
|---|---:|---|
| Unauthenticated access | 401 | PASS |
| Alice accesses her own profile | 200 | PASS |
| Alice attempts to access Bob's profile | 403 | PASS |
| Bob accesses his own profile | 200 | PASS |
| Bob attempts to access Alice's profile | 403 | PASS |
| Invalid profile ID test | 403 | PASS |

**Recorded result: 6/6 tests passed locally.**

The invalid-ID test expects `403` because the current application performs the ownership check before checking whether the requested user exists.

## Lessons Learned

- Never treat a URL identifier as proof of authorization.
- Enforce access control on the server for every protected resource.
- Use environment variables for application secrets.
- Test both authorized and unauthorized access paths.
- Keep security documentation aligned with observed results.

## Limitations

This is a small educational lab using fictional accounts and local test data. Its login routes simulate user selection rather than implementing real identity verification, so they are not suitable for production.

Passing six tests does not prove that an application is completely secure. The lab does not yet cover every possible access-control issue, session attack, or unauthorized operation.

## Future Improvements

- Add tests for unauthorized editing and deletion.
- Introduce additional user roles and protected resources.
- Add automated tests to a continuous integration workflow.
- Improve authentication and session management.
- Expand the test suite to cover additional edge cases.
