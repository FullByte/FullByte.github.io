---
name: mcp-server-discovery
description: Discover MCP server capabilities and transport endpoint for 0xfab1.net.
---

# MCP Server Discovery

Use this skill to discover MCP server card metadata on 0xfab1.net.

## Discovery Endpoint

- MCP Server Card: `/.well-known/mcp/server-card.json`

## Notes

- The server card contains server identity, transport endpoint, and capabilities.
- The endpoint is suitable for pre-connection discovery by MCP clients.
