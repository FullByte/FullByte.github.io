---
name: api-catalog-discovery
description: Discover API catalog, OpenAPI description, and status endpoint for 0xfab1.net.
---

# API Catalog Discovery

Use this skill to discover API metadata published by 0xfab1.net.

## Discovery Endpoints

- API catalog: `/.well-known/api-catalog`
- OpenAPI document: `/well-known/openapi.json`
- Status endpoint: `/api/status.json`

## Notes

- The API catalog is published as a Linkset JSON document.
- OpenAPI is provided as a static description for automated tooling.
- Status is a lightweight JSON endpoint suitable for health checks.
