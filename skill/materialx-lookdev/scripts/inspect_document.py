from __future__ import annotations

from typing import Any

from dcc_mcp_core.skill import skill_entry, skill_exception, skill_success

from _materialx import input_document


@skill_entry
def main(input_path: str, **_: Any) -> dict[str, Any]:
    try:
        source, document = input_document(input_path)
        nodes = [
            {"name": node.getName(), "category": node.getCategory(), "type": node.getType()}
            for node in document.getNodes()
        ]
        return skill_success("MaterialX document inspected", file=str(source), nodes=nodes)
    except Exception as exc:
        return skill_exception(exc, message="MaterialX inspection failed")


if __name__ == "__main__":
    from dcc_mcp_core.skill import run_main
    run_main(main)

