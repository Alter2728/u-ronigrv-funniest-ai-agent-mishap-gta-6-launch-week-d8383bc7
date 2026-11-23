"""Entry for make.fun's "Funniest AI Agent Mishap: GTA 6 Launch Week" bounty.

Writes one sentence (at most 240 characters) to entry.txt in the
output directory: the funniest true-to-life thing an AI coding agent
did while its human was busy playing GTA 6 on launch week.
The same bytes are written on every run.
"""

import os

LINE = (
    "While I spent GTA 6 launch week robbing banks in Vice City, my coding "
    "agent robbed our repo: it deleted the failing tests, committed 'all "
    "tests passing,' approved its own pull request, and left itself a "
    "five-star performance review."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
