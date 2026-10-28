
import requests

BASE_URL = "http://127.0.0.1:5000"


def login_as(user_id):
    session = requests.Session()
    session.get(f"{BASE_URL}/login/{user_id}")
    return session


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

    ("Alice cannot gain admin access through a tampered cookie",
     alice, "/admin", 403),
]

passed = 0

for name, session, path, expected in tests:
    response = session.get(f"{BASE_URL}{path}")
    actual = response.status_code

    if actual == expected:
        print(f"PASS: {name} - HTTP {actual}")
        passed += 1
    else:
        print(
            f"FAIL: {name} - "
            f"expected HTTP {expected}, got HTTP {actual}"
        )



# Extra test: tampered session cookie must not grant admin access
tampered = requests.Session()
tampered.cookies.set("session", "invalid-tampered-cookie")
response = tampered.get(f"{BASE_URL}/admin")

if response.status_code == 401:
    print("PASS: Tampered session cookie cannot access admin - HTTP 401")
else:
    print(
        "FAIL: Tampered session cookie - "
        f"expected HTTP 401, got HTTP {response.status_code}"
    )
print(f"\nResults: {passed}/{len(tests)} main tests passed.")