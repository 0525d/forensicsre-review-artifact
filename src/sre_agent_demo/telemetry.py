from __future__ import annotations

from collections.abc import Callable

from .models import TelemetryQuery, TelemetryResult


class TelemetryGateway:
    """Adapter boundary for metrics, logs, and traces backends."""

    def __init__(self, query_fn: Callable[[TelemetryQuery], TelemetryResult] | None = None):
        self._query_fn = query_fn

    def query(self, request: TelemetryQuery) -> TelemetryResult:
        if self._query_fn is None:
            raise RuntimeError("No telemetry adapter configured")
        return self._query_fn(request)


class InMemoryTelemetryGateway(TelemetryGateway):
    """Minimal deterministic adapter for a local demo or integration test."""

    def __init__(self, results: dict[str, TelemetryResult]):
        self._results = results

    def query(self, request: TelemetryQuery) -> TelemetryResult:
        try:
            return self._results[request.expression]
        except KeyError as error:
            raise KeyError(f"No demo telemetry result for {request.expression!r}") from error

