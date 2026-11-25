"""Fix Human Sleep: Funniest Patch Note.

Writes one line of patch notes announcing that human sleep is fixed
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Stdlib only, no network, deterministic.
"""

import os

ENTRY = (
    "Fixed: sleep no longer crashes at 3 a.m. \u2014 the background process "
    "replaying your most embarrassing moment from 2014 has been terminated."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
