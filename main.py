import os
from pathlib import Path

ENTRY = "Core competency: strategic ambiguity. Development goal: mention deadlines before they become archaeology."
OUTPUT_NAME = "entry.txt"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / OUTPUT_NAME).write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
