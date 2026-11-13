# Security policy for the public case study

This repository documents an engineering project; it does **not** distribute the Cercle 8 commercial source code.

Never publish:
- Real customer, tenant, merchant or payment records
- Secrets, API keys, session cookies, webhook signing keys or provider tokens
- Database dumps, unredacted logs or internal environment files
- Proprietary algorithm formulas and confidential system details

For a sensitive concern, use private GitHub vulnerability reporting if enabled or contact the maintainer privately through [GitHub](https://github.com/lilouwen).

Deleting a secret from the latest commit does not remove it from Git history; exposed credentials must be rotated or revoked.

[← Repository home](README.md)