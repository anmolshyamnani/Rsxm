# AI Operating System

A 24×7 autonomous operating system for running company operations, projects, software products, and research workflows.

## Mission

This platform acts as an AI Chief of Staff and orchestration layer. It coordinates specialized agents, long-running workflows, memory, tools, research, project execution, and monitoring while keeping high-risk actions behind human approval.

## Initial operating domains

- Company operations
- Project management
- Product/software development
- Research and literature review
- Knowledge management
- Analytics and reporting
- 24×7 monitoring and recovery

## Architecture

```text
Next.js Control Center
        |
    FastAPI API
        |
  AI Orchestrator
        |
  Workflow Engine
        |
 Agent Runtime ---- Tool Registry
        |                  |
        +---- Memory -----+
        |
 PostgreSQL + pgvector
        |
 Redis / Events / Workers
        |
 Observability + Audit
```

## Core agents

1. Chief of Staff
2. Project Manager
3. Research
4. Literature Review
5. Developer
6. Marketing
7. Data & Analytics
8. Monitoring & Recovery

## Safety model

Agents use least-privilege tool access. External communication, financial actions, destructive operations, and other high-impact actions can require explicit human approval.

## Status

Phase 1 scaffold: API contracts, domain model, agent registry, task/workflow concepts, Docker development environment, and frontend control-center shell.
