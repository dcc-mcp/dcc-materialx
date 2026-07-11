from __future__ import annotations

from pathlib import Path
from typing import Any

from dcc_mcp_core.skill import skill_entry, skill_exception, skill_success

from _materialx import materialx, validation


@skill_entry
def main(
    output_path: str,
    material_name: str,
    base_color: list[float] | None = None,
    base_color_texture: str | None = None,
    roughness: float = 0.5,
    metalness: float = 0.0,
    **_: Any,
) -> dict[str, Any]:
    try:
        mx = materialx()
        document = mx.createDocument()
        shader = document.addNode("standard_surface", f"{material_name}_shader", "surfaceshader")
        shader.setInputValue("base_color", mx.Color3(*(base_color or [0.8, 0.8, 0.8])))
        shader.setInputValue("specular_roughness", float(roughness))
        shader.setInputValue("metalness", float(metalness))
        if base_color_texture:
            image = document.addNode("image", f"{material_name}_base_color", "color3")
            image.setInputValue("file", base_color_texture, "filename")
            shader.addInput("base_color", "color3").setNodeName(image.getName())
        document.addMaterialNode(material_name, shader)
        valid, message = validation(document)
        if not valid:
            raise ValueError(message or "MaterialX document is invalid")
        target = Path(output_path).expanduser().resolve()
        target.parent.mkdir(parents=True, exist_ok=True)
        mx.writeToXmlFile(document, str(target))
        return skill_success("MaterialX material created", file=str(target), material=material_name)
    except Exception as exc:
        return skill_exception(exc, message="MaterialX authoring failed")


if __name__ == "__main__":
    from dcc_mcp_core.skill import run_main
    run_main(main)
