"""Structural validation for all teaching notebooks."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_notebooks_are_valid_and_have_executable_cells():
    notebooks = sorted((ROOT / "labs").rglob("*.ipynb"))
    assert len(notebooks) >= 4
    for path in notebooks:
        data = json.loads(path.read_text(encoding="utf-8"))
        assert data["nbformat"] == 4
        assert data["cells"]
        assert any(cell["cell_type"] == "code" for cell in data["cells"])
        for cell in data["cells"]:
            assert cell["cell_type"] in {"markdown", "code"}
            assert "source" in cell
            if cell["cell_type"] == "code":
                assert cell.get("outputs", []) == []
                assert cell.get("execution_count") is None
