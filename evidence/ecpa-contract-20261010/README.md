# ECPA activation-contract evidence

Evidence label: `manager-contract-mock-worker-non-performance`.

The vLLM-HUST Extension Manager 0.3 inspect, check, plan, dry-run launch, and a
real managed `native_state_engine --assembly-check-only` process passed for MOD
version 0.2.0. The manager verified the exact `RESEARCH_MANIFEST.json` SHA-256,
host/API/protocol ranges, exclusive scheduler/worker resource claims, and
rendered the sole activation argument as `--additional-config` with
`experiment_mode=true`.

StateAxis tests cover strict parsing, stale-digest and unsafe-policy rejection,
matched ON/OFF identity, mock-worker exact outputs, candidate-batch effect
counting, inherited environment removal, identity-owned worker activation, and
clean shutdown. The complete Rust library suite passed 405 tests; all-target
compilation and the native service build passed. The MOD passed three Python
tests and Ruff lint.

This record is not accelerator execution and makes no latency, throughput,
memory, capacity, or production-performance claim. Frozen issue #56 real-NPU
results remain correctness-negative and are not superseded.

Reproduce manager validation from the repository root:

```bash
VLLM_HUST_EXT_CONFIG=evidence/ecpa-contract-20261010/manager-config.json \
  vllm-hust-ext extension check org.vllm-hust.stateaxis-dynamic-microbatch
VLLM_HUST_EXT_CONFIG=evidence/ecpa-contract-20261010/manager-config.json \
  vllm-hust-ext extension plan org.vllm-hust.stateaxis-dynamic-microbatch
VLLM_HUST_EXT_CONFIG=evidence/ecpa-contract-20261010/manager-config.json \
  vllm-hust-ext run --dry-run -- /bin/true
```
