"""The copyright guard in validate_engine.py must fail on stored or cited book extractions."""

from __future__ import annotations

from pathlib import Path

from scripts.validate_engine import scan_book_extractions

ROOT = Path(__file__).resolve().parents[1]


def _write(path: Path, text: str = "# Note\n") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_repository_is_clean() -> None:
    assert scan_book_extractions(ROOT) == []


def test_extraction_folder_anywhere_is_flagged(tmp_path: Path) -> None:
    _write(tmp_path / "docs" / "book-study" / "01-craft.md")
    _write(tmp_path / "skills" / "x" / "extracted-books" / "a.md")
    found = scan_book_extractions(tmp_path)
    assert "docs/book-study/ folder present" in found
    assert "skills/x/extracted-books/ folder present" in found


def test_extraction_file_name_is_flagged(tmp_path: Path) -> None:
    _write(tmp_path / "governance" / "six-book-extractions.md")
    assert any("six-book-extractions.md" in item for item in scan_book_extractions(tmp_path))


def test_citations_and_chapter_headings_are_flagged(tmp_path: Path) -> None:
    _write(tmp_path / "skills" / "a" / "references" / "r.md", "See Book-study 02 for the tour finding.\n")
    _write(tmp_path / "skills" / "b" / "references" / "r.md", "# Topic\n\n## Chapter 3 Grids\n")
    _write(tmp_path / "doctrine" / "d.md", "Read docs/book-study/00-synthesis.md first.\n")
    found = scan_book_extractions(tmp_path)
    assert len(found) == 3


def test_task_reference_with_source_line_passes(tmp_path: Path) -> None:
    _write(
        tmp_path / "skills" / "a" / "references" / "grid-procedure.md",
        "# Grid construction procedure\n\n## Inputs\n\nSources: Muller-Brockmann (1981) *Grid Systems*.\n",
    )
    _write(tmp_path / "rules" / "common" / "core.md", "No `docs/book-study/` folder.\n")
    assert scan_book_extractions(tmp_path) == []
