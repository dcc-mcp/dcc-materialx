# dcc-materialx

Portable MaterialX authoring and validation for look-development interchange
across Maya, Houdini, Blender, USD/Hydra, Unreal, and renderer pipelines.

![MaterialX interchange](docs/materialx-workflow.png)

## Included skill

`materialx-lookdev` creates a minimal Standard Surface material, validates `.mtlx`
documents, and lists their nodes. Host adapters remain responsible for import,
renderer translation, and scene assignment.

```mermaid
flowchart LR
    T[Textures] --> M[MaterialX Standard Surface]
    M --> V[Validation]
    V --> H[Hydra and USD]
    V --> D[Maya Houdini Blender Unreal]
```

