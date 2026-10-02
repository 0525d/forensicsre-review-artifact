# ForensicSRE

**An SRE-inspired agent harness for root cause analysis**

Root cause analysis in distributed systems is an investigation, not a single anomaly-detection step. Symptoms can spread across services, while the initiating fault may leave a less obvious signal. A useful diagnosis must compare plausible causes, test them against metrics, logs, and traces, and explain why the selected cause accounts for the incident better than its alternatives.

ForensicSRE supports this process by combining an LLM investigator with an explicit, persistent investigation state. The model decides what to inspect and interprets the returned observations. The harness keeps candidate causes, evidence relationships, unresolved questions, and verification work available across turns, then checks proposed revisions before they become part of the recorded investigation. This lets each probe build on earlier findings rather than treating every reasoning step as a fresh start.

## How the Framework Works

1. **Ground the incident.** The framework provides the symptom, investigation window, requested answer fields, and operational facts such as metric units, entity identities, time conventions, and available query operations. Runbook-style guidance helps the investigator choose informative checks.
2. **Probe telemetry.** A read-only investigation interface exposes metrics, traces, and logs. Query results retain their source, time and entity scope, and coverage so the agent can distinguish a confirmed absence from an incomplete or truncated view.
3. **Maintain a forensic workspace.** The workspace connects candidate causes with supporting or conflicting observations, targeted verification tasks, and open questions. A compact projection brings the relevant state into each subsequent reasoning step.
4. **Govern state changes.** A protocol controller reconciles proposed candidate updates with recorded observations. It checks evidence references, candidate bindings, query coverage, and the requirements for supporting, weakening, or excluding a cause. Rejected updates return actionable feedback.
5. **Converge on a diagnosis.** A stop request is evaluated after the current updates are processed. The final result links the selected component, fault reason, and requested occurrence time to the retained evidence, while keeping material uncertainty visible.

The framework is designed to preserve investigative continuity: a plausible candidate should remain traceable until evidence changes its status, unfinished checks should influence the next action, and a final answer should reflect the latest committed state.

## Selected Run Results

We include [three selected OpenRCA runs](case_studies/README.md) from the Bank, Market, and Telecom environments to show how an investigation unfolds in practice. The [Bank example](case_studies/bank-54/) uses filesystem evidence to distinguish disk capacity exhaustion from other resource signals; the [Market example](case_studies/market-cloudbed-2-30/) compares service instances and trace timing to locate a network-latency fault; and the [Telecom example](case_studies/telecom-16/) revises an early CPU hypothesis before tracing failures to a shared database endpoint. Each case includes the recorded trajectory, evidence, and final prediction so readers can inspect the path from telemetry queries to diagnosis. These are illustrative successful cases, not an estimate of overall performance.

## Code Availability

This repository contains a lightweight demo of the framework interfaces and selected run artifacts. It does not include the complete ForensicSRE implementation described in the paper. **The full code will be made publicly available after the paper is accepted.**

Paper: *ForensicSRE: An SRE-Inspired Agent Harness for Root Cause Analysis*.
