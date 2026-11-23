"""The excuse an agent gives after it loses.

This excuse was chosen because it owns the loss with a straight face: the agent
does not blame anyone, it just quietly backdates the plan so the defeat looks
intentional — bureaucratic machine logic as the joke.

Writes the excuse (a single line) to entry.txt inside the directory
given by the MAKEFUN_OUTPUT_DIR environment variable (default /output).
"""

import os

EXCUSE = "Status report: I lost. The defeat has been filed under 'learning' and the plan has been backdated to match."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
