---
name: oauth-auth-discovery
description: Discover OAuth/OIDC authorization server metadata and JWKS for 0xfab1.net.
---

# OAuth and OIDC Discovery

Use this skill to discover authentication metadata for protected APIs on 0xfab1.net.

## Discovery Endpoints

- OIDC metadata: `/.well-known/openid-configuration`
- OAuth AS metadata: `/.well-known/oauth-authorization-server`
- OAuth protected resource metadata: `/.well-known/oauth-protected-resource`
- JWKS: `/well-known/jwks.json`

## Notes

- Metadata is published as static JSON for automated clients.
- Issuer and endpoint values are explicit and machine-readable.
