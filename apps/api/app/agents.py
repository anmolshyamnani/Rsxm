from dataclasses import dataclass

from .models import Domain


@dataclass(frozen=True)
class AgentDefinition:
    name: str
    description: str
    domain: Domain
    permissions: dict


AGENTS = [
    AgentDefinition("Chief of Staff", "Coordinates company, projects and research.", Domain.COMPANY, {"read": ["all"], "write": ["tasks"]}),
    AgentDefinition("Project Manager", "Plans and monitors project execution.", Domain.PROJECT, {"read": ["projects"], "write": ["tasks"]}),
    AgentDefinition("Research Agent", "Finds, organizes and analyzes research evidence.", Domain.RESEARCH, {"read": ["research"], "write": ["research_notes"]}),
    AgentDefinition("Literature Review Agent", "Builds evidence matrices and literature reviews.", Domain.RESEARCH, {"read": ["papers"], "write": ["research_notes"]}),
    AgentDefinition("Developer Agent", "Inspects and assists with software projects.", Domain.PRODUCT, {"read": ["github"], "write": ["pull_requests"]}),
    AgentDefinition("Marketing Agent", "Plans and analyzes marketing work.", Domain.COMPANY, {"read": ["analytics"], "write": ["drafts"]}),
    AgentDefinition("Data & Analytics Agent", "Analyzes operational and research data.", Domain.COMPANY, {"read": ["analytics", "datasets"], "write": ["reports"]}),
    AgentDefinition("Monitoring & Recovery Agent", "Monitors system health and failed workflows.", Domain.PRODUCT, {"read": ["system"], "write": ["recovery_tasks"]}),
]
