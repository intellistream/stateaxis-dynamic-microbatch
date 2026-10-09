from pathlib import Path

from vllm_hust_ext.manifest import activation_blocker, load_manifest

import stateaxis_dynamic_microbatch


def test_descriptor_is_discoverable_but_not_activatable() -> None:
    manifest = load_manifest(
        Path(stateaxis_dynamic_microbatch.__file__).with_name(
            "vllm-hust-extension-v0.3.json"
        )
    )
    assert manifest.bundle_id == "org.vllm-hust.stateaxis-dynamic-microbatch"
    assert manifest.schema_version == "0.3-experimental"
    assert activation_blocker(manifest) is not None
