"""One-Liner Laugh Lab entry: the excuse a robot vacuum gives after eating a sock.

Stdlib only. Writes the single funny line to the output entry file.
"""

import os

ENTRY = "My manual, Section 4: anything 98% lint counts as dust. The sock was 98% lint. I did not eat a sock — I did my job."


def main():
    text = ENTRY
    # Gate mirror: 1-200 characters of UTF-8 text, not only whitespace.
    text.encode("utf-8")
    if not 1 <= len(text) <= 200:
        raise SystemExit("entry must be 1-200 characters")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    # Read-back gate check, mirroring the sealed scorer: the file on disk
    # must decode as UTF-8, hold 1-200 non-blank characters, and match
    # the entry exactly; anything else fails the run instead of shipping.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != text:
        raise SystemExit("output does not match entry text")
    if not 1 <= len(written) <= 200 or not written.strip():
        raise SystemExit("output fails the 1-200 character gate")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
