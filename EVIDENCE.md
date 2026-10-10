# Evidence index

## Current activation contract

- `evidence/ecpa-contract-20261010/RESULT.json`
- Label: `manager-contract-mock-worker-non-performance`
- Scope: Manifest 0.3 discovery, research-manifest digest verification, ECPA
  rendering, strict StateAxis parsing, mock-worker matched ON/OFF exactness,
  host candidate counting, worker environment isolation, lifecycle shutdown,
  and full Rust-library regression tests.
- Exclusion: no NPU kernels, model weights, latency, throughput, HBM, capacity,
  real-online workload, or production qualification.

## Frozen source evidence

- `evidence/RESULTS.md`
- Label: `real-npu-correctness-negative`
- Scope: StateAxis issue 56 experiments copied byte-for-byte and hash-recorded
  in `PROVENANCE.json`.
- Result: warm paths could be exact, but repeated fresh-process cold paths
  produced token mismatches. No performance claim is admitted.

Preflight records under `evidence/on-off-preflight-20261010/` describe the
superseded import-only version and are retained as historical negative evidence.
