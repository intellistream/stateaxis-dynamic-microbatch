# Issue 56 dynamic microbatch: frozen R8 stop result

This directory is the complete isolated-cache R8 real-NPU result. It contains
the matched control/candidate pair, cold and warm phase requests, model/runtime
identities, activation evidence, NPU snapshots, failure provenance and cleanup
records. `SHA256SUMS` covers every imported file except itself.

Control completed both phases with 128/128 exact outputs. Candidate completed
its lifecycle and its warm phase was 128/128 exact, but its fresh-process cold
phase had four exact-token mismatches (ordinals 5, 6, 7 and 10). The frozen
correctness gate therefore stopped the remaining repetitions. Any throughput
observation from this incomplete pair is non-qualifying.

`runs/c16-o32-r1-candidate/client_stdout.json` is intentionally the original
zero-byte failed-arm artifact: the runner stopped before aggregate client JSON
was written. The cold-phase result, `FAILED`, exit status and
`failure_provenance.json` are the authoritative failure records.
