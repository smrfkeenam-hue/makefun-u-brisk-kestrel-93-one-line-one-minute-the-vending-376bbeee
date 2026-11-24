"""One-line vending machine pickup line for make.fun.

Writes the entry text to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output).
"""

import os

# The line itself: the machine speaks through its own parts — its hum,
# its coil — and the punch lands on "exact change" at the very end.
ENTRY = "I've hummed for a thousand strangers, but my coil only gets stuck on you — got exact change for a lifetime of snacks?"

OUTPUT_NAME = "entry.txt"
DEFAULT_OUT_DIR = "/output"


def resolve_out_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUT_DIR)


def write_entry(text, out_dir):
    """Write one line of text to the entry file inside out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def main():
    write_entry(ENTRY, resolve_out_dir())


if __name__ == "__main__":
    main()
