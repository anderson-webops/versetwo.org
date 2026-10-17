"""Create a local test copy with doubled rem-based text; never ship this copy."""

from pathlib import Path
import shutil


root = Path(__file__).resolve().parents[1]
destination = root / "tmp" / "accessibility-200"
destination.mkdir(parents=True, exist_ok=True)
for source in (root / "prototype").iterdir():
    if source.is_file():
        shutil.copyfile(source, destination / source.name)
stylesheet = destination / "style.css"
stylesheet.write_text(stylesheet.read_text() + "\nhtml{font-size:200%!important}\n")
print(destination)
