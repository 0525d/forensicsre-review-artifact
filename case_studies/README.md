# ForensicSRE: three case studies

Selected successful DeepSeek-V4-Flash runs from three OpenRCA environments. These are illustrative cases, not a representative sample or an estimate of aggregate accuracy. The scores and baseline predictions below come from the recorded evaluation; each ForensicSRE run has one recorded attempt.

| Case | Reference answer | ForensicSRE answer | Score | What the investigation shows |
| --- | --- | --- | ---: | --- |
| [Telecom 16](telecom-16/) | `db_007`, `db close`, 2020-05-24 01:47:00 | `db_007`, `db close`, 01:47:02 | 1.00 | Tests an early CPU hypothesis against the pre-incident baseline, then traces failures from multiple callers to a shared database endpoint. |
| [Bank 54](bank-54/) | `IG02`, `high disk space usage`, 2021-03-06 15:19:00 | Same component, reason, and time | 1.00 | Uses rising filesystem usage and falling free space on `/tomcat` to distinguish capacity exhaustion from disk I/O and unrelated CPU activity. |
| [Market/cloudbed-2 30](market-cloudbed-2-30/) | `cartservice-0`, `container network latency`, 2022-03-20 16:50:36 | `cartservice-0`, `container network latency`, 16:50:00 | 1.00 | Compares cartservice instances and trace timing; `cartservice-0` latency rises sharply at 16:50 while peer instances do not. |

The benchmark accepts the Telecom and Market timestamp predictions at its configured precision, despite the seconds-level difference from the labels. All times above use the dataset's local time.

## Baseline comparison

All rows below use the same case and DeepSeek model. The score is the existing benchmark score; 0.33 means one of three requested fields is correct.

| Case | System | Prediction: component / reason / time | Score |
| --- | --- | --- | ---: |
| Telecom 16 | ForensicSRE | `db_007` / `db close` / 01:47:02 | 1.00 |
| Telecom 16 | ReAct | `docker_003` / `CPU fault` / 01:33:31 | 0.00 |
| Telecom 16 | mABC | `docker_007` / `network loss` / 01:44:00 | 0.00 |
| Telecom 16 | OpenRCA | `db_001` / `db connection limit` / 01:30:28 | 0.00 |
| Bank 54 | ForensicSRE | `IG02` / `high disk space usage` / 15:19:00 | 1.00 |
| Bank 54 | ReAct | `Redis01` / `high CPU usage` / 15:05:00 | 0.00 |
| Bank 54 | mABC | `Tomcat04` / `high disk I/O read usage` / 15:26:00 | 0.00 |
| Bank 54 | OpenRCA | `MG01` / `high disk I/O read usage` / 15:08:00 | 0.00 |
| Market/cloudbed-2 30 | ForensicSRE | `cartservice-0` / `container network latency` / 16:50:00 | 1.00 |
| Market/cloudbed-2 30 | ReAct | `cartservice-0` / `container CPU load` / 16:30:00 | 0.33 |
| Market/cloudbed-2 30 | mABC | `cartservice2-0` / `container CPU load` / 16:31:00 | 0.00 |
| Market/cloudbed-2 30 | OpenRCA | `adservice-0` / `container memory load` / 16:30:00 | 0.00 |

## Files and provenance

Each case directory contains the ForensicSRE `result.csv`, `run_metadata.json`, prompt JSON, execution history log, full trajectory notebook, `direct_evidence.jsonl`, and `direct_stop_authorization.jsonl`. Local filesystem paths in these artifacts have been anonymized. The latter two are the evidence and stop-decision records from the same run. Open the notebook to inspect the actual queries and observations; the summary above does not replace the trajectory.

The Market run reaches the correct benchmark answer, but its final authorization is marked `BUDGET_BEST_EFFORT` with unresolved alternative leads. It should be presented as a successful diagnosis with that limitation, rather than as a fully closed investigation.
