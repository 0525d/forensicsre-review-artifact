from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class IncidentRequest:
    incident_id: str
    system: str
    start: str
    end: str
    symptoms: list[str] = field(default_factory=list)
    requested_fields: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class TelemetryQuery:
    source_type: str
    expression: str
    start: str
    end: str
    filters: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class TelemetryResult:
    source_type: str
    source: str
    start: str
    end: str
    observations: list[dict[str, Any]] = field(default_factory=list)


@dataclass(frozen=True)
class RootCause:
    occurrence_datetime: str
    component: str
    reason: str


@dataclass(frozen=True)
class Evidence:
    source_type: str
    source: str
    start: str
    end: str
    observation: str


@dataclass(frozen=True)
class RCAResult:
    incident_id: str
    status: str
    confidence: float
    root_causes: list[RootCause] = field(default_factory=list)
    evidence: list[Evidence] = field(default_factory=list)
    diagnostic_trace_id: str | None = None

