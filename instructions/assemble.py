#!/usr/bin/env python3
"""
assemble.py – Glue the five DevPartner instruction modules into one prompt file.

Usage:
  python assemble.py                 # writes FULL_PROMPT.md at repo root
  python assemble.py --dest path.md  # custom destination path

Features
--------
* Concatenates the five core instruction modules in **lexical order** so
  cross‑references remain valid and token budgets stay predictable.
* Provides an **accurate token estimate**: uses *tiktoken* if available, and
  falls back to a simple char/4 heuristic otherwise.
* Emits a build footer with UTC timestamp and token estimate.

Exit Codes:
  0  – success
  1  – missing module(s)
  2  – other runtime error
"""
from __future__ import annotations

import argparse
import datetime as _dt
import sys
from pathlib import Path
from typing import List

MODULE_DIR = Path(__file__).resolve().parent  # /instructions by convention
MODULE_FILES = [
    "01_core.md",
    "02_lifecycle.md",
    "03_roles.md",
    "04_comms.md",
    "05_rulebook.yml",
]

FOOTER_TEMPLATE = (
    "\n---\n_generated on {ts} UTC – ≈{tok_est} tokens in prompt_\n"
)

# ---------------------------------------------------------------------------
# Token estimator – prefers tiktoken for accuracy, char/4 heuristic fallback
# ---------------------------------------------------------------------------

def _tk_len(text: str) -> int:  # pragma: no cover – best‑effort import
    try:
        import tiktoken  # type: ignore

        enc = tiktoken.encoding_for_model("gpt-4")
        return len(enc.encode(text))
    except ModuleNotFoundError:
        return -1  # sentinel for fallback
    except Exception:  # any unexpected tiktoken runtime issue
        return -1


def estimate_tokens(text: str) -> int:
    """Return an estimated token count for *text*.

    * If *tiktoken* is available, we use its GPT‑4 encoding for high fidelity.
    * Otherwise we fall back to `len(text) / 4`, which is a common rough
      estimate for English prose.
    """
    real = _tk_len(text)
    if real > 0:
        return real
    # fallback heuristic
    return int(len(text) / 4)

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def read_modules(base: Path, files: List[str]) -> List[str]:
    contents: List[str] = []
    missing: List[str] = []
    for fname in files:
        fpath = base / fname
        if not fpath.exists():
            missing.append(fname)
            continue
        contents.append(fpath.read_text())
    if missing:
        print(f"[assemble] Missing module(s): {', '.join(missing)}", file=sys.stderr)
        sys.exit(1)
    return contents


def build_prompt(modules: List[str]) -> str:
    joined = "\n\n".join(modules)
    ts = _dt.datetime.utcnow().strftime("%Y‑%m‑%d %H:%M:%S")
    footer = FOOTER_TEMPLATE.format(ts=ts, tok_est=estimate_tokens(joined))
    return joined + footer

# ---------------------------------------------------------------------------
# CLI entry‑point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Assemble DevPartner prompt")
    parser.add_argument(
        "--dest",
        default=MODULE_DIR.parent / "FULL_PROMPT.md",
        type=Path,
        help="Destination output file (default: ../../FULL_PROMPT.md)",
    )
    args = parser.parse_args()

    modules = read_modules(MODULE_DIR, MODULE_FILES)
    prompt = build_prompt(modules)

    args.dest.write_text(prompt)
    print(
        f"[assemble] Wrote {args.dest} (≈{estimate_tokens(prompt)} tokens)"
    )


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(2)
