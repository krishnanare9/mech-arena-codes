from pathlib import Path
from PIL import Image
import re
import subprocess

root = Path(".")
image_dir = root / "images"
text_files = [p for p in root.rglob("*") if p.is_file() and p.suffix.lower() in {".html", ".css", ".js"} and ".git" not in p.parts and ".github" not in p.parts]
pattern = re.compile(r'''(?P<url>(?:/)?images/[^"'()\\s,]+\\.png)''', re.IGNORECASE)
referenced = set()
for path in text_files:
    content = path.read_text(encoding="utf-8")
    referenced.update(match.group("url").lstrip("/") for match in pattern.finditer(content))

converted = []
for relative in sorted(referenced):
    source = root / relative
    if not source.exists():
        print(f"Skipping missing referenced image: {relative}")
        continue
    target = source.with_suffix(".webp")
    with Image.open(source) as im:
        im.save(target, "WEBP", quality=86, method=6)
    converted.append((relative, target.stat().st_size))

if not converted:
    print("No referenced PNG assets found; nothing to optimize.")
    raise SystemExit(0)

for path in text_files:
    content = path.read_text(encoding="utf-8")
    updated = pattern.sub(lambda m: m.group("url")[:-4] + ".webp", content)
    if updated != content:
        path.write_text(updated, encoding="utf-8")

subprocess.run(["git", "config", "user.name", "github-actions[bot]"], check=True)
subprocess.run(["git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"], check=True)
subprocess.run(["git", "add", "images", "*.html", "*.css", "*.js"], check=True)
changed = subprocess.run(["git", "diff", "--cached", "--quiet"])
if changed.returncode == 0:
    print("No file changes to commit.")
else:
    subprocess.run(["git", "commit", "-m", "Optimize referenced site images as WebP"], check=True)
    subprocess.run(["git", "push"], check=True)

for name, size in converted:
    print(f"{name} -> {Path(name).with_suffix('.webp')} ({size} bytes)")
