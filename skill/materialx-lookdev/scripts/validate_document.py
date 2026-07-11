from __future__ import annotations

from typing import Any

from dcc_mcp_core.skill import skill_entry, skill_exception, skill_success

from _materialx import input_document, validation


@skill_entry
def main(input_path: str, **_: Any) -> dict[str, Any]:
    try:
        source, document = input_document(input_path)
        valid, message = validation(document)
        if not valid:
            raise ValueError(message or "MaterialX document is invalid")
        return skill_success("MaterialX document is valid", file=str(source), validation=message)
    except Exception as exc:
        return skill_exception(exc, message="MaterialX validation failed")


if __name__ == "__main__":
    from dcc_mcp_core.skill import run_main
    run_main(main)

