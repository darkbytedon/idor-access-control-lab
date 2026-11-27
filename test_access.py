import sys
import requests

BASE_URL = "http://127.0.0.1:5000"


def login_as(user_id):
    session = requests.Session()
    session.get(f"{BASE_URL}/login/{user_id}", timeout=5)
    return session


def main():
    alice = login_as(1)
    bob = login_as(2)
    admin = login_as(3)

    tests = [
        ("Unauthenticated user is denied",
         requests.Session(), "/profile/1", 401),

        ("Alice can access her own profile",
         alice, "/profile/1", 200),

        ("Alice cannot access Bob's profile",
         alice, "/profile/2", 403),

        ("Bob can access his own profile",
         bob, "/profile/2", 200),

        ("Bob cannot access Alice's profile",
         bob, "/profile/1", 403),

        ("Alice cannot access an invalid profile ID",
         alice, "/profile/999", 403),

        ("Unauthenticated user cannot access admin",
         requests.Session(), "/admin", 401),

        ("Alice cannot access admin",
         alice, "/admin", 403),

        ("Bob cannot access admin",
         bob, "/admin", 403),

        ("Admin can access admin dashboard",
         admin, "/admin", 200),

        ("Alice cannot gain admin access through URL parameter",
         alice, "/admin?role=admin", 403),

        ("Alice cannot access admin through her normal session",
         alice, "/admin", 403),
    ]

    passed = 0
    failed = 0

    for name, session, path, expected in tests:
        try:
            response = session.get(
                f"{BASE_URL}{path}", timeout=5
            )
            actual = response.status_code

            if actual == expected:
                print(f"PASS: {name} - HTTP {actual}")
                passed += 1
            else:
                print(
                    f"FAIL: {name} - expected HTTP "
                    f"{expected}, got HTTP {actual}"
                )
                failed += 1

        except requests.RequestException as error:
            print(f"FAIL: {name} - {error}")
            failed += 1

    tampered = requests.Session()
    tampered.cookies.set(
        "session", "invalid-tampered-cookie"
    )

    try:
        response = tampered.get(
            f"{BASE_URL}/admin", timeout=5
        )

        if response.status_code == 401:
            print(
                "PASS: Invalid session cookie is rejected - HTTP 401"
            )
            passed += 1
        else:
            print(
                "FAIL: Invalid session cookie - expected HTTP 401, "
                f"got HTTP {response.status_code}"
            )
            failed += 1

    except requests.RequestException as error:
        print(f"FAIL: Invalid session cookie test - {error}")
        failed += 1

    print(f"\nResults: {passed}/13 checks passed.")
    print(f"Failures: {failed}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
