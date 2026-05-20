(function () {
  "use strict";

  var REGISTRATION_KEY = "__fullbyteWebMcpRegistration";
  var SEARCH_INDEX_URL = "/search/search_index.json";
  var DEFAULT_LIMIT = 5;
  var MAX_LIMIT = 20;
  var searchIndexPromise = null;

  function supportsWebMcp() {
    if (typeof navigator === "undefined" || !navigator.modelContext) {
      return false;
    }

    return (
      typeof navigator.modelContext.provideContext === "function" ||
      typeof navigator.modelContext.registerTool === "function"
    );
  }

  function normalizeSameOriginUrl(inputPath) {
    if (typeof inputPath !== "string") {
      throw new Error("path must be a string");
    }

    var raw = inputPath.trim();
    if (!raw) {
      throw new Error("path is required");
    }

    var url = new URL(raw, window.location.origin);
    if (url.origin !== window.location.origin) {
      throw new Error("Only same-origin URLs are allowed");
    }

    if (url.protocol !== "https:" && url.protocol !== "http:") {
      throw new Error("Unsupported URL protocol");
    }

    return url.pathname + url.search + url.hash;
  }

  function guessMarkdownPath(pathname) {
    if (!pathname || pathname === "/") {
      return "/index.md";
    }

    if (pathname.endsWith("/")) {
      return pathname + "index.md";
    }

    if (pathname.endsWith(".html")) {
      return pathname.slice(0, -5) + ".md";
    }

    var lastSegment = pathname.split("/").pop() || "";
    if (!lastSegment.includes(".")) {
      return pathname + ".md";
    }

    return pathname;
  }

  function getPageDescription() {
    var descriptionMeta = document.querySelector('meta[name="description"]');
    if (descriptionMeta && descriptionMeta.content) {
      return descriptionMeta.content.trim();
    }

    var ogDescriptionMeta = document.querySelector(
      'meta[property="og:description"]'
    );
    if (ogDescriptionMeta && ogDescriptionMeta.content) {
      return ogDescriptionMeta.content.trim();
    }

    return "";
  }

  function getPageHeadings(limit) {
    var headingLimit = typeof limit === "number" ? limit : 20;
    var nodes = document.querySelectorAll("article h1, article h2, article h3");
    var headings = [];

    for (var i = 0; i < nodes.length && headings.length < headingLimit; i += 1) {
      var node = nodes[i];
      var text = (node.textContent || "").trim();
      if (!text) {
        continue;
      }

      headings.push({
        level: Number(node.tagName.slice(1)),
        text: text,
        id: node.id || null,
      });
    }

    return headings;
  }

  function clampLimit(value) {
    if (typeof value !== "number" || Number.isNaN(value)) {
      return DEFAULT_LIMIT;
    }

    return Math.min(MAX_LIMIT, Math.max(1, Math.floor(value)));
  }

  async function loadSearchIndex() {
    if (!searchIndexPromise) {
      searchIndexPromise = fetch(SEARCH_INDEX_URL, {
        credentials: "same-origin",
      }).then(function (response) {
        if (!response.ok) {
          throw new Error(
            "Unable to load search index (" + response.status + ")"
          );
        }

        return response.json();
      });
    }

    return searchIndexPromise;
  }

  function scoreSearchResult(entry, query, terms) {
    var title = String(entry.title || "");
    var text = String(entry.text || "");
    var titleLower = title.toLowerCase();
    var textLower = text.toLowerCase();
    var score = 0;

    if (titleLower.includes(query)) {
      score += 8;
    }

    if (textLower.includes(query)) {
      score += 3;
    }

    for (var i = 0; i < terms.length; i += 1) {
      var term = terms[i];
      if (!term) {
        continue;
      }

      if (titleLower.includes(term)) {
        score += 4;
      }

      if (textLower.includes(term)) {
        score += 1;
      }
    }

    return score;
  }

  function buildSearchResults(docs, query, limit) {
    var terms = query.split(/\s+/).filter(Boolean);
    var ranked = [];

    for (var i = 0; i < docs.length; i += 1) {
      var entry = docs[i];
      var score = scoreSearchResult(entry, query, terms);
      if (score <= 0) {
        continue;
      }

      ranked.push({
        score: score,
        entry: entry,
      });
    }

    ranked.sort(function (a, b) {
      if (a.score === b.score) {
        return 0;
      }
      return a.score > b.score ? -1 : 1;
    });

    return ranked.slice(0, limit).map(function (item) {
      var entry = item.entry;
      var snippet = String(entry.text || "").trim();

      return {
        title: String(entry.title || ""),
        url: String(entry.location || ""),
        snippet: snippet.slice(0, 280),
      };
    });
  }

  function createTools() {
    return [
      {
        name: "navigate-site",
        description: "Navigate to another page on 0xfab1.net.",
        annotations: { readOnlyHint: false },
        inputSchema: {
          type: "object",
          properties: {
            path: {
              type: "string",
              description:
                "Relative or absolute same-origin URL to open (for example /tech/index.html).",
            },
            newTab: {
              type: "boolean",
              description: "Open the destination in a new tab when true.",
              default: false,
            },
          },
          required: ["path"],
          additionalProperties: false,
        },
        execute: async function (args) {
          var safeArgs = args || {};
          var destination = normalizeSameOriginUrl(safeArgs.path);
          var openInNewTab = Boolean(safeArgs.newTab);

          if (openInNewTab) {
            window.open(destination, "_blank", "noopener");
          } else {
            window.location.assign(destination);
          }

          return {
            ok: true,
            destination: destination,
            openedInNewTab: openInNewTab,
          };
        },
      },
      {
        name: "search-site",
        description:
          "Search published site content using MkDocs search_index.json and return top matches.",
        annotations: { readOnlyHint: true },
        inputSchema: {
          type: "object",
          properties: {
            query: {
              type: "string",
              description: "Natural language query to search for.",
            },
            limit: {
              type: "integer",
              minimum: 1,
              maximum: MAX_LIMIT,
              default: DEFAULT_LIMIT,
              description: "Maximum number of results to return.",
            },
          },
          required: ["query"],
          additionalProperties: false,
        },
        execute: async function (args) {
          var safeArgs = args || {};
          var queryRaw = String(safeArgs.query || "").trim().toLowerCase();
          if (!queryRaw) {
            throw new Error("query is required");
          }

          var limit = clampLimit(safeArgs.limit);
          var index = await loadSearchIndex();
          var docs = Array.isArray(index.docs) ? index.docs : [];
          var results = buildSearchResults(docs, queryRaw, limit);

          return {
            query: safeArgs.query,
            totalIndexedDocuments: docs.length,
            returned: results.length,
            results: results,
          };
        },
      },
      {
        name: "get-current-page",
        description:
          "Return metadata for the current page, including title, URL, headings, and markdown source URL.",
        annotations: { readOnlyHint: true },
        inputSchema: {
          type: "object",
          properties: {
            includeHeadings: {
              type: "boolean",
              default: true,
              description:
                "Include h1-h3 headings extracted from the current article body.",
            },
          },
          additionalProperties: false,
        },
        execute: async function (args) {
          var safeArgs = args || {};
          var includeHeadings = safeArgs.includeHeadings !== false;
          var path = window.location.pathname;

          return {
            title: document.title,
            url: window.location.href,
            path: path,
            markdownUrl: guessMarkdownPath(path),
            description: getPageDescription(),
            headings: includeHeadings ? getPageHeadings(20) : [],
          };
        },
      },
      {
        name: "get-agent-discovery-endpoints",
        description:
          "Return key .well-known endpoints published by this site for agents.",
        annotations: { readOnlyHint: true },
        inputSchema: {
          type: "object",
          properties: {},
          additionalProperties: false,
        },
        execute: async function () {
          return {
            site: window.location.origin,
            endpoints: {
              apiCatalog: "/.well-known/api-catalog",
              agentSkillsIndex: "/.well-known/agent-skills/index.json",
              oauthAuthorizationServer:
                "/.well-known/oauth-authorization-server",
              openIdConfiguration: "/.well-known/openid-configuration",
              oauthProtectedResource:
                "/.well-known/oauth-protected-resource",
              mcpServerCard: "/.well-known/mcp/server-card.json",
            },
          };
        },
      },
    ];
  }

  function registerWebMcpTools() {
    if (!supportsWebMcp()) {
      return;
    }

    var modelContext = navigator.modelContext;
    var tools = createTools();

    try {
      if (typeof modelContext.provideContext === "function") {
        modelContext.provideContext({ tools: tools });
        window[REGISTRATION_KEY] = "provideContext";
        return;
      }

      if (window[REGISTRATION_KEY]) {
        return;
      }

      if (typeof modelContext.registerTool === "function") {
        for (var i = 0; i < tools.length; i += 1) {
          try {
            modelContext.registerTool(tools[i]);
          } catch (error) {
            var message =
              error && error.message ? String(error.message) : String(error);
            if (!/already|exist|duplicate/i.test(message)) {
              throw error;
            }
          }
        }
        window[REGISTRATION_KEY] = "registerTool";
      }
    } catch (error) {
      console.warn("[WebMCP] Tool registration failed:", error);
    }
  }

  function init() {
    if (window.top !== window.self) {
      return;
    }

    registerWebMcpTools();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init, { once: true });
  } else {
    init();
  }
})();
