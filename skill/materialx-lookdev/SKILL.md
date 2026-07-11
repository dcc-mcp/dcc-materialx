---
name: materialx-lookdev
description: Interchange skill for creating, inspecting, and validating portable MaterialX look-development documents. Use between texture authoring and DCC or USD material import.
license: MIT
compatibility: "dcc-mcp-core 0.19+, MaterialX 1.38+, Python 3.9+"
metadata:
  dcc-mcp:
    dcc: python
    layer: domain
    stage: interchange
    version: "0.1.0"
    tags: [materialx, material, lookdev, standard-surface, usd, hydra]
    search-hint: "create MaterialX material, validate mtlx, inspect material graph, exchange lookdev"
    tools: tools.yaml
---

# MaterialX Look Development

Create a portable Standard Surface starting point and validate `.mtlx` files
before DCC import. Renderer-specific translation and material assignment remain
owned by the target adapter.

