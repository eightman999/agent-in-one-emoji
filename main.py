import os
from pathlib import Path


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text("🤖\n", encoding="utf-8")


if __name__ == "__main__":
    main()
