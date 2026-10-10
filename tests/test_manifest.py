import hashlib
import json
from pathlib import Path

import pytest
from vllm_hust_ext.manifest import activation_blocker, load_manifest

import stateaxis_dynamic_microbatch


def test_policy_is_discoverable_and_experimentally_activatable() -> None:
    manifest = load_manifest(
        Path(stateaxis_dynamic_microbatch.__file__).with_name(
            "vllm-hust-extension-v0.3.json"
        )
    )
    assert manifest.bundle_id == "org.vllm-hust.stateaxis-dynamic-microbatch"
    assert manifest.bundle_version == "0.2.0"
    assert manifest.schema_version == "0.3-experimental"
    assert activation_blocker(manifest) is None
    additional = dict(manifest.activation.additional_config)
    research_manifest = Path(stateaxis_dynamic_microbatch.__file__).parents[2] / (
        "RESEARCH_MANIFEST.json"
    )
    assert (
        additional["stateaxis_mod"]["manifest_sha256"]
        == hashlib.sha256(research_manifest.read_bytes()).hexdigest()
    )
    assert additional["stateaxis_mod"]["performance_qualified"] is False
    assert additional["stateaxis_dynamic_microbatch"] == {
        "enabled": True,
        "dynamic_batching": True,
        "dual_microbatch": True,
        "batch_window_us": 10_000,
        "scheduler_max_batch_size": 32,
        "decode_batch_rows": 16,
        "lane_rows": 8,
        "require_greedy": True,
        "forbid_cow": True,
        "fail_closed": True,
    }


def test_research_manifest_matches_package_contract() -> None:
    research_manifest = Path(stateaxis_dynamic_microbatch.__file__).parents[2] / (
        "RESEARCH_MANIFEST.json"
    )
    payload = json.loads(research_manifest.read_text())
    assert payload["mod_id"] == stateaxis_dynamic_microbatch.MOD_ID
    assert payload["version"] == "0.2.0"
    assert payload["mechanism"]["decode_batch_rows"] == 16
    assert payload["mechanism"]["lane_rows"] == 8
    assert payload["qualification"]["performance_qualified"] is False
    assert payload["qualification"]["evidence_label"] == "real-npu-correctness-negative"
    provenance = json.loads((research_manifest.parent / "PROVENANCE.json").read_text())
    assert (
        provenance["implementation_boundary"]["research_manifest_sha256"]
        == hashlib.sha256(research_manifest.read_bytes()).hexdigest()
    )


def test_python_contract_fails_closed() -> None:
    assert stateaxis_dynamic_microbatch.dynamic_microbatch().decode_batch_rows == 16
    with pytest.raises(ValueError, match="B16-to-8\\+8"):
        stateaxis_dynamic_microbatch.DynamicMicrobatchConfig(lane_rows=4)
