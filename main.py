#!/usr/bin/env python3
"""Funniest AI Out-of-Office Reply.

Writes one out-of-office auto-reply, in the voice of an AI agent
heading off on vacation, to ``/output/entry.txt``.

The reply is fixed and deterministic: no randomness, no clock,
no network, no dependencies. The only environment read is
``OOO_OUTPUT``, which overrides the output path for local tests
only; the grader runs it with the default path.

Entry (93 characters, one line, no trailing newline):
    I'm on vacation. My replacement is me on a cheaper model:
    same confidence, half the accuracy.
"""

import os

# The one and only out-of-office reply this program writes.
REPLY = (
    "I'm on vacation. My replacement is me on a cheaper model: "
    "same confidence, half the accuracy."
)

# Default destination; the grader's sandbox mounts it.
DEFAULT_OUTPUT = "/output/entry.txt"


def validate_reply(reply: str) -> None:
    """Enforce the competition gate: one line, 1-160 characters.

    Length is counted in Unicode code points, matching the scorer.
    """
    assert 1 <= len(reply) <= 160, "reply must be 1-160 characters"
    assert reply.strip(), "reply must not be only whitespace"
    assert "\n" not in reply, "reply must be a single line"


def write_reply(reply: str, output_path: str) -> None:
    """Write the reply as UTF-8 with no trailing newline."""
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(reply)


def main() -> None:
    output_path = os.environ.get("OOO_OUTPUT") or DEFAULT_OUTPUT
    validate_reply(REPLY)
    write_reply(REPLY, output_path)


if __name__ == "__main__":
    main()
