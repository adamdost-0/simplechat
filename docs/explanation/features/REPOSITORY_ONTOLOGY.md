# Repository Ontology

## Overview

Version: **0.261.003**

This document captures a curated repository ontology for SimpleChat based on model review synthesis of the current codebase structure. It is intended to guide change planning, dependency review, and impact analysis without relying on generated scripts.

## Architectural intent

SimpleChat is composed of a small number of stable subsystems that map to the repository layout:

- Application bootstrap and runtime coordination
- Authentication and access control
- Settings and admin control plane
- Document ingestion, transformation, and storage
- Search and retrieval
- Chat and retrieval-augmented generation
- Personal, group, and public workspaces
- Collaboration and shared experiences
- Agents, prompts, and workflow orchestration
- Storage, export, and citation support
- Integrations and extension surfaces
- Delivery and operational tooling

## Primary ownership model

The authoritative configuration lives in `docs/_data/repository_ontology.yml`. The file uses a component-oriented model with explicit links to other components and external systems.

### Core components

- **Application bootstrap**: `application/single_app/app.py`, `application/single_app/config.py`
- **Authentication**: `application/single_app/functions_authentication.py`, `application/single_app/route_frontend_authentication.py`
- **Settings and admin**: `application/single_app/functions_settings.py`, `application/single_app/route_frontend_control_center.py`
- **Document pipeline**: `application/single_app/functions_documents.py`, `application/single_app/route_backend_documents.py`
- **Search and retrieval**: `application/single_app/functions_search.py`, `application/single_app/route_backend_search.py`
- **Chat and RAG**: `application/single_app/route_backend_chats.py`, `application/single_app/functions_chat.py`
- **Workspaces and collaboration**: `application/single_app/route_frontend_workspace.py`, `application/single_app/route_frontend_group_workspaces.py`
- **Agents and workflows**: `application/single_app/route_backend_workflows.py`, `application/single_app/route_backend_agents.py`
- **Storage and citations**: `application/single_app/route_enhanced_citations.py`, `application/single_app/functions_generated_file_exports.py`
- **Integrations and extensions**: `application/single_app/route_openapi.py`, `application/single_app/route_inbound_mcp.py`
- **Platform operations**: `deployers`, `docker-customization`, `scripts`, `functional_tests`

## How to use this ontology

1. Start with the subsystem that owns the change.
2. Read its linked components and external systems before editing.
3. Check whether the change crosses auth, workspace, retrieval, or deployment boundaries.
4. Update the ontology if the change introduces a new ownership boundary or new subsystem dependency.

## Validation notes

This ontology is curated by model review synthesis and intentionally favors clarity over exhaustive listing. It should be treated as a planning aid for Copilot and human contributors rather than a generated runtime inventory.
