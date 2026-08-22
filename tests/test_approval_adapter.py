import json
import unittest
from pathlib import Path


class ApprovalAdapterTests(unittest.TestCase):
    def test_live_design_controls_are_gated(self):
        payload = json.loads((Path(__file__).parents[1] / "docs" / "approval-adapter.json").read_text(encoding="utf-8"))
        self.assertEqual(payload["engine"], "design")
        actions = {item["action_type"]: item for item in payload["actions"]}
        for action_type in ("design.tokens.publish", "design.accessibility.exception.approve", "design.agent.checkpoint.release"):
            self.assertEqual(actions[action_type]["class"], "L3")
            self.assertTrue(actions[action_type]["preview_required"])


if __name__ == "__main__":
    unittest.main()
