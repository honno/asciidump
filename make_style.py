#!/usr/bin/env python
from pathlib import Path

import sass


def main():
    css_path = Path(__file__).parent / "src" / "asciidump" / "style.css"
    css = sass.compile(filename="sass/style.scss")
    if not css_path.exists():
        with open(css_path, "w") as f:
            f.write(css)
        exit(1)
    with open(css_path) as f:
        style_is_correct = f.read() == css
    if not style_is_correct:
        with open(css_path, "w") as f:
            f.write(css)
        exit(1)


if __name__ == "__main__":
    main()
