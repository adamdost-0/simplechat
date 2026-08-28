#!/usr/bin/env python3
"""
Functional test for repository ontology assets.
Version: 0.261.003
Implemented in: 0.261.003

This test ensures the curated ontology configuration, instruction guidance,
and feature documentation exist and describe the expected subsystem boundaries.
"""

import os
import sys
from pathlib import Path

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def test_repository_ontology_assets():
    """Validate that the ontology files are present and populated."""
    repo_root = Path(__file__).resolve().parents[1]

    ontology_path = repo_root / "docs" / "_data" / "repository_ontology.yml"
    instructions_path = repo_root / ".github" / "instructions" / "repository-ontology.instructions.md"
    feature_doc_path = repo_root / "docs" / "explanation" / "features" / "REPOSITORY_ONTOLOGY.md"

    missing = [str(path) for path in [ontology_path, instructions_path, feature_doc_path] if not path.exists()]
    if missing:
        raise FileNotFoundError(f"Missing ontology assets: {', '.join(missing)}")

    ontology_text = ontology_path.read_text(encoding="utf-8")
    instructions_text = instructions_path.read_text(encoding="utf-8")
    feature_doc_text = feature_doc_path.read_text(encoding="utf-8")

    required_markers = [
        "components:",
        "application-bootstrap",
        "chat-rag",
        "platform-operations",
        "docs/_data/repository_ontology.yml",
        "Repository ontology guidance",
    ]

    for marker in required_markers:
        if marker not in ontology_text and marker not in instructions_text and marker not in feature_doc_text:
            raise AssertionError(f"Missing expected ontology marker: {marker}")

    print("Repository ontology test passed")
    return True


if __name__ == "__main__":
    success = test_repository_ontology_assets()
    sys.exit(0 if success else 1)
