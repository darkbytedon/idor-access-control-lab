# Professional Application Security Assessment

## IDOR / Broken Object Level Authorization

| Assessment detail | Information |
|---|---|
| Assessment date | 27 November 2026 |
| Application | Flask IDOR training application |
| Environment | Ubuntu local laboratory |
| Assessment type | Controlled educational security assessment |
| Finding ID | IDOR-01 |
| Status | Remediation demonstrated and retested |
| Classification | Portfolio work sample, not a client engagement |

## 1. Executive Summary

This assessment demonstrates an Insecure Direct Object Reference (IDOR) vulnerability in a deliberately vulnerable Flask training application.

The vulnerability occurred because the application authenticated a user but failed to verify whether that user was authorized to access the requested profile.

During controlled testing, Alice successfully requested Bob's profile and received HTTP 200 OK together with Bob's fictional profile information.

A separate corrected implementation introduced server-side ownership validation. Retesting demonstrated that unauthorized cross-user access returned HTTP 403 Forbidden while legitimate profile access continued to work.

An automated assessment suite covering both implementations completed successfully with 10 out of 10 tests passing.

## 2. Assessment Objectives

The assessment aimed to:

1. Demonstrate an IDOR vulnerability in a controlled application.
2. Reproduce unauthorized cross-user profile access.
3. Identify the authorization weakness.
4. Implement server-side ownership validation.
5. Verify legitimate and unauthorized access behaviour.
6. Perform automated regression testing.
7. Document evidence, impact, remediation and limitations.

## 3. Scope and Environment

The assessment used two separate Flask applications.

| Application | Directory | Port |
|---|---|---:|
| Intentionally vulnerable | vulnerable-demo/ | 5001 |
| Remediated | remediated-demo/ | 5002 |

Both applications were restricted to the local loopback interface at 127.0.0.1.

### Fictional test accounts

| User | Account ID | Email |
|---|---:|---|
| Alice | 1 | alice@example.test |
| Bob | 2 | bob@example.test |

### Technologies and tools

- Python
- Flask
- Requests
- Python unittest
- Ubuntu
- Git and GitHub

### Scope limitations

Testing was restricted to the local applications and fictional in-memory user records.

No public website, third-party system, production database or real customer information was involved.

## 4. Vulnerability Description

Insecure Direct Object Reference (IDOR) occurs when an application allows a user to access an object through a user-controlled identifier without properly verifying authorization.

This weakness is commonly associated with Broken Object Level Authorization (BOLA).

For example, Alice may legitimately request her own profile using:

`/profile/1`

Changing the requested identifier to:

`/profile/2`

should not allow Alice to access Bob's private information.

Authentication establishes the identity of the requester. Authorization determines which resources that requester is permitted to access.

The intentionally vulnerable implementation checked authentication but did not enforce profile ownership.


## 5. Vulnerability Reproduction

The vulnerable application was started locally on port 5001.

A Python Requests session was used to authenticate as Alice and request profile resources.

### Testing procedure

1. Authenticate as Alice using the local training login route.
2. Request Alice's own profile at `/profile/1`.
3. Change the requested identifier to `/profile/2`.
4. Inspect the HTTP response and returned profile information.

### Observed results

| Test | HTTP status | Observation |
|---|---:|---|
| Alice login | 302 | Login redirect successful |
| Alice accesses Alice | 200 | Legitimate access |
| Alice accesses Bob | 200 | Unauthorized access succeeded |

The unauthorized response contained:

- Logged-in user ID: 1
- Profile owner: Bob
- Email: bob@example.test

This demonstrated unauthorized cross-user profile disclosure in the controlled vulnerable application.

## 6. Root Cause Analysis

The root cause was the absence of a server-side ownership authorization check.

The vulnerable application verified that a user had an authenticated session but did not compare the authenticated user's ID with the requested profile owner's ID.

Consequently, an authenticated user could change the object identifier and retrieve another user's profile.

## 7. Security Impact Assessment

### Demonstrated impact

The controlled test demonstrated disclosure of another fictional user's name and email address.

### Potential real-world impact

An equivalent weakness in a production application could expose private customer profiles, account information, documents or other user-owned resources.

The actual impact would depend on the sensitivity and volume of accessible information and the application's deployment and authorization controls.

### Severity

No production severity rating or CVSS score is assigned.

The laboratory used fictional information. A production severity assessment would require evidence about the real application's data sensitivity, exposure and business impact.


## 8. Remediation

A separate corrected Flask application was created in `remediated-demo/app.py`.

The correction introduced a server-side ownership check:

`if logged_in_user_id != user_id:`

When the authenticated user ID does not match the requested profile ID, the application returns HTTP 403 Forbidden.

The corrected application:
- Rejects unauthenticated requests.
- Allows users to access their own profiles.
- Denies requests for other users' profiles.
- Performs authorization on the server.

For production applications, authentication must use a properly implemented identity mechanism. Authorization must be enforced for every protected resource.

## 9. Retesting

The same Alice-to-Bob request was repeated against the corrected application on port 5002.

| Test | Observed HTTP status |
|---|---:|
| Alice login redirect | 302 |
| Alice accesses her own profile | 200 |
| Alice accesses Bob's profile | 403 |

The unauthorized request returned: `Forbidden: you cannot access this profile.`

Legitimate access remained available while unauthorized cross-user access was denied.

### Automated test results

Command executed: `python -m unittest -v test_assessment.py`

**Result: 10 tests executed, 10 passed.**

| Application | Tests | Result |
|---|---:|---|
| Intentionally vulnerable | 4 | 4 passed; expected weakness reproduced |
| Remediated | 6 | 6 passed; expected access controls verified |
| Total | 10 | 10 passed |

The vulnerable tests passing means the expected insecure behaviour was reproduced. It does not mean the vulnerable application is secure.

The captured output is stored in `evidence/assessment-tests.txt`.


## 10. Historical Context and Evidence Integrity

The original GitHub application history was reviewed during this assessment.

The earliest published application version inspected already contained a profile ownership comparison.

Therefore, the original GitHub history does not establish that the published application was vulnerable.

The vulnerable implementation in `vulnerable-demo/app.py` was created separately on 27 November 2026 to reproduce the missing authorization condition in a controlled educational environment.

The corrected demonstration is maintained separately in `remediated-demo/app.py`.

The before-and-after results documented in this report come from these controlled demonstrations.

## 11. Assessment Limitations

This was an educational laboratory exercise, not a client engagement or production penetration test.

The following limitations apply:

1. Only fictional users and in-memory profile data were used.
2. The training login route allows selection of a user ID and is not production-grade authentication.
3. Testing focused on profile ownership authorization.
4. No production database or real customer information was involved.
5. The results do not establish that every possible application vulnerability has been eliminated.
6. The vulnerable demonstration was restricted to the local loopback interface.

The intentionally vulnerable application must not be deployed publicly.

## 12. Conclusion

The assessment successfully demonstrated how missing object-level authorization can allow an authenticated user to access another user's profile.

The root cause was the absence of a server-side ownership check.

A corrected implementation was created and retested. Unauthorized cross-user access was denied while legitimate profile access remained functional.

The automated assessment completed with 10 out of 10 tests passing.

This project demonstrates practical skills in IDOR analysis, Python and Flask security testing, authorization remediation, automated regression testing and evidence-based security reporting.

## Disclaimer

This report documents a controlled educational exercise using fictional users and local applications.

It is not a report of a real client engagement, production penetration test or third-party security assessment.

All testing was conducted in a locally controlled environment.

---

Author: DarkByteDon
Project: IDOR Access Control Security Assessment
Environment: Ubuntu / Python / Flask
Date: 27 November 2026
