import importlib.util
from pathlib import Path

import MaterialX as mx


MODULE = Path(__file__).parents[1] / "skill/materialx-lookdev/scripts/_materialx.py"
SPEC = importlib.util.spec_from_file_location("_materialx", MODULE)
helper = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(helper)


def test_reads_valid_document(tmp_path):
    document = mx.createDocument()
    document.addNode("constant", "value", "color3")
    path = tmp_path / "material.mtlx"
    mx.writeToXmlFile(document, str(path))
    source, loaded = helper.input_document(str(path))
    assert source == path.resolve()
    assert loaded.getNode("value") is not None


def test_validation_shape():
    valid, message = helper.validation(mx.createDocument())
    assert isinstance(valid, bool)
    assert isinstance(message, str)
