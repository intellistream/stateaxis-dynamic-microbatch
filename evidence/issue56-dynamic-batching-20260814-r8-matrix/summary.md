# Issue #56 r8 candidate rejection

The isolated-cache runner removed the r7 ownership failure. The first control completed cold and warm with 128/128 exact outputs per phase. The matched candidate completed lifecycle, but its cold phase had four exact-token mismatches (ordinals 5, 6, 7 and 10); the same process's warm phase was 128/128 exact.

This non-deterministic cold correctness failure follows an exact r7 candidate run with the same frozen runtime/artifacts. Therefore the opt-in dual-microbatch candidate is rejected, remains default-off, and the remaining repetitions were not run. No performance or speedup claim is permitted. Raw failure evidence and cleanup state are retained in this directory.
