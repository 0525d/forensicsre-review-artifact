from __future__ import annotations

from collections.abc import Callable

from .models import IncidentRequest, RCAResult, TelemetryQuery, TelemetryResult
from .telemetry import TelemetryGateway


class DiagnosticAgent:
    """Orchestrates planning, telemetry access, verification, and result formatting.

    Domain-specific reasoning and backend access are injected so the framework can
    be connected to an LLM and an existing observability platform later.
    """

    def __init__(
        self,
        telemetry: TelemetryGateway,
        planner: Callable[[IncidentRequest], list[TelemetryQuery]],
        synthesizer: Callable[[IncidentRequest, list[TelemetryResult]], RCAResult],
    ):
        self.telemetry = telemetry
        self.planner = planner
        self.synthesizer = synthesizer

    def diagnose(self, incident: IncidentRequest) -> RCAResult:
        queries = self.planner(incident)
        observations = [self.telemetry.query(query) for query in queries]
        return self.synthesizer(incident, observations)
