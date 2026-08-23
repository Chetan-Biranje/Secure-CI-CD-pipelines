# Complete IDOR & Broken Object Level Authorization (BOLA) Testing Methodology

**Author:** Chetan Biranje  
**Reference:** OWASP API Top 10 (API1:2023)

---

## 4-Phase Testing Workflow

### Phase 1: Object & Endpoint Discovery
1. Intercept all application traffic via Burp Suite Professional.
2. Identify all REST endpoints accepting identifiers (`/api/v1/orders/{id}`, `/users/{userId}/profile`).
3. Note authorization header structures (`Authorization: Bearer <token>`).

### Phase 2: Role & Account Setup
1. Create two test accounts with identical permission tiers:
   * **Account A (Victim):** `user_id = 1001`
   * **Account B (Attacker):** `user_id = 1002`
2. Create an Administrative account:
   * **Account Admin:** `user_id = 9999`

### Phase 3: Matrix Authorization Verification
1. Capture legitimate request from Account A.
2. Replay request using Account B's JWT authorization token while retaining Account A's `user_id`.
3. Test across all HTTP verbs (`GET`, `PUT`, `POST`, `DELETE`, `PATCH`).

### Phase 4: Remediation Guidelines for Developers
```python
# ❌ INSECURE: Trusting client parameter blindly
def get_user_profile(request, profile_id):
    return Database.get(profile_id)

# ✅ SECURE: Enforcing server-side ownership check
def get_user_profile(request, profile_id):
    current_user_id = request.user.id
    profile = Database.get(profile_id)
    if profile.owner_id != current_user_id and not request.user.is_admin:
        raise PermissionDenied("Unauthorized access to requested resource.")
    return profile
```
