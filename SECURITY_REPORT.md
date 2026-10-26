\# IDOR Vulnerability: Detection, Remediation and Automated Testing



\## Project Overview



\- \*\*Technology:\*\* Python, Flask, Requests

\- \*\*Vulnerability:\*\* Insecure Direct Object Reference (IDOR)

\- \*\*Environment:\*\* Local training application at `http://127.0.0.1:5000`



\## Objective



Demonstrate an IDOR vulnerability, implement server-side authorization, and test that users cannot access each other's profiles.



\## Vulnerability Description



IDOR occurs when an application accepts a user-controlled object identifier without verifying that the user is authorized to access the requested object.



In this lab, Alice and Bob are fictional users. The profile route checks whether the logged-in user's ID matches the requested profile ID.



\## Remediation



The application checks authentication and profile ownership on the server before returning profile information. Requests for another user's profile receive HTTP 403 Forbidden.



\## Automated Tests



The `test\_access.py` script tests six scenarios:



1\. Unauthenticated access is denied.

2\. Alice can access her own profile.

3\. Alice cannot access Bob's profile.

4\. Bob can access his own profile.

5\. Bob cannot access Alice's profile.

6\. Alice cannot access an invalid profile ID.



\*\*Observed result:\*\* Six out of six tests passed in the recorded test run.



\## Limitations



This is a small local training lab using fictional accounts. Passing these six tests does not prove that a real application is secure or that every possible access-control issue has been tested.



\## Future Improvements



\- Test unauthorized editing and deletion.

\- Add more user roles and resources.

\- Add automated tests to a continuous integration workflow.

\- Publish the source code, test script, and documentation in a GitHub repository.

