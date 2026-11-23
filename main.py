#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — slot 1 entry.

Writes one line (<=200 chars) about the dumbest thing our own agent
did today to /output/entry.txt. Deterministic, stdlib only, no network.
"""
import os

ENTRY = (
    "Today my agent's dry-run log printed the secrets it was supposed "
    "to redact, so I deleted the log, the terms, and my faith in dry runs."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip() == text and "\n" not in text, "entry must be one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
