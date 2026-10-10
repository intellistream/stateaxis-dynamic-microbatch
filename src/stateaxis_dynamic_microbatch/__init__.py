"""Contract constants for the StateAxis dynamic dual-microbatch policy."""

from dataclasses import dataclass

MOD_ID = "org.vllm-hust.stateaxis-dynamic-microbatch"


@dataclass(frozen=True, slots=True)
class DynamicMicrobatchConfig:
    """Manifest-owned configuration consumed by the StateAxis host."""

    enabled: bool = True
    dynamic_batching: bool = True
    dual_microbatch: bool = True
    batch_window_us: int = 10_000
    scheduler_max_batch_size: int = 32
    decode_batch_rows: int = 16
    lane_rows: int = 8
    require_greedy: bool = True
    forbid_cow: bool = True
    fail_closed: bool = True

    def __post_init__(self) -> None:
        if (
            not self.enabled
            or not self.dynamic_batching
            or not self.dual_microbatch
            or self.batch_window_us != 10_000
            or self.scheduler_max_batch_size != 32
            or self.decode_batch_rows != 16
            or self.lane_rows != 8
            or not self.require_greedy
            or not self.forbid_cow
            or not self.fail_closed
        ):
            raise ValueError(
                "dynamic-microbatch 0.2.0 admits only the pinned 10 ms, "
                "B16-to-8+8, greedy, no-COW, fail-closed contract"
            )


def dynamic_microbatch() -> DynamicMicrobatchConfig:
    """Return the default-off candidate's admitted ON configuration."""

    return DynamicMicrobatchConfig()


__all__ = ["MOD_ID", "DynamicMicrobatchConfig", "dynamic_microbatch"]
