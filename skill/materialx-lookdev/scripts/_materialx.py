from __future__ import annotations

from pathlib import Path
from typing import Any


def materialx():
    try:
        import MaterialX as mx  # Lazy import: optional compiled interchange dependency.
        return mx
    except ImportError as exc:
        raise RuntimeError("MaterialX Python bindings are required: pip install MaterialX") from exc


def input_document(path: str):
    source = Path(path).expanduser().resolve()
    if not source.is_file():
        raise FileNotFoundError(source)
    mx = materialx()
    document = mx.createDocument()
    mx.readFromXmlFile(document, str(source))
    return source, document


def validation(document) -> tuple[bool, str]:
    result: Any = document.validate()
    if isinstance(result, tuple):
        return bool(result[0]), str(result[1])
    return bool(result), ""
