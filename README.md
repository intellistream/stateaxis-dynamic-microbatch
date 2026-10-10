# stateaxis-dynamic-microbatch

Extension ID: `org.vllm-hust.stateaxis-dynamic-microbatch`

This experimental MOD owns the reviewed dynamic batching and dual-microbatch
overlap mechanism extracted from StateAxis issue
[#56](https://github.com/Qixin-Gaoke/stateaxis/issues/56). It is maintained in
the `intellistream` organization by Shuhao Zhang (Tony), directly responsible;
no advisor is declared.

## Mechanism and activation

Version 0.2.0 is default-off and activatable only through vLLM-HUST Extension
Manager/ECPA. The manager verifies `RESEARCH_MANIFEST.json` and forwards a
hash-bound experimental contract. StateAxis then admits exactly:

- a 10,000 us scheduler collection window and maximum batch size 32;
- early release at a full B16 decode cohort;
- an eligible greedy, adapter-free, no-COW B16 decode split into two B8 worker
  lanes;
- fail-closed worker startup, with the legacy environment variable removed and
  restored only from the admitted MOD identity.

Disable the extension to roll back. The host then has no MOD identity, dynamic
batching remains off, and the worker receives no dual-microbatch switch.

## Evidence boundary

Status: **correctness-negative; not performance-qualified**.

The frozen real-NPU evidence is retained in `evidence/RESULTS.md`. Warm paths
could be exact, but repeated fresh-process cold paths produced token mismatches.
One earlier throughput observation was 47.156% below control and was not
repeated; it is not a performance result. The full matched real-online matrix
was therefore not completed.

`evidence/ecpa-contract-20261010/` proves only manager activation, strict host
identity binding, matched mock-worker ON/OFF behavior, effect counting,
lifecycle shutdown, and failure-closed environment handling. It is not NPU
execution and makes no latency, throughput, capacity, memory, or production
claim. Negative, failed, and inconclusive results remain part of the record.

## Install and validate

```bash
python -m pip install -e . --no-deps
pytest -q
ruff check .

VLLM_HUST_EXT_CONFIG=evidence/ecpa-contract-20261010/manager-config.json \
  vllm-hust-ext extension check org.vllm-hust.stateaxis-dynamic-microbatch
VLLM_HUST_EXT_CONFIG=evidence/ecpa-contract-20261010/manager-config.json \
  vllm-hust-ext extension plan org.vllm-hust.stateaxis-dynamic-microbatch
VLLM_HUST_EXT_CONFIG=evidence/ecpa-contract-20261010/manager-config.json \
  vllm-hust-ext run --dry-run -- /bin/true
```

See `EVIDENCE.md` for the evidence labels and exact scope.
