#!/usr/bin/env python3
"""Fetch the Google Fonts CSS for the deck's fonts and self-host the woff2 files.

Both families are variable fonts on Google Fonts, so we ask for a weight *range*
per family and get one (subsetted) file per subset instead of one copy per weight.
"""
import os
import re
import shutil
import urllib.request

FAMILIES = {
    "Nunito+Sans": "200..600",   # body: 200 / 400 / 600 used by the theme
    "Fira+Code": "300..700",     # mono: Fira Code's full weight axis
}
CSS_URL = (
    "https://fonts.googleapis.com/css2?"
    + "&".join(f"family={f}:wght@{r}" for f, r in FAMILIES.items())
    + "&display=swap"
)
UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)
KEEP_SUBSETS = {"latin", "latin-ext"}
FONT_DIR = "public/fonts"
OUT_CSS = "styles/index.css"

shutil.rmtree(FONT_DIR, ignore_errors=True)
os.makedirs(FONT_DIR, exist_ok=True)
os.makedirs(os.path.dirname(OUT_CSS), exist_ok=True)

req = urllib.request.Request(CSS_URL, headers={"User-Agent": UA})
css = urllib.request.urlopen(req, timeout=30).read().decode()

pattern = re.compile(r"/\*\s*(?P<subset>[\w-]+)\s*\*/\s*(?P<block>@font-face\s*\{.*?\})", re.S)
out_blocks, seen, total = [], {}, 0

for m in pattern.finditer(css):
    subset, block = m.group("subset"), m.group("block")
    if subset not in KEEP_SUBSETS:
        continue
    family = re.search(r"font-family:\s*'([^']+)'", block).group(1)
    style = re.search(r"font-style:\s*([^;]+);", block).group(1).strip()
    weight = re.search(r"font-weight:\s*([^;]+);", block).group(1).strip()
    url = re.search(r"url\((https://[^)]+)\)", block).group(1)
    ext = os.path.splitext(url)[1]
    slug = f"{family.lower().replace(' ', '-')}-{style}-{subset}{ext}"
    if slug not in seen:
        data = urllib.request.urlopen(
            urllib.request.Request(url, headers={"User-Agent": UA}), timeout=30
        ).read()
        with open(os.path.join(FONT_DIR, slug), "wb") as fh:
            fh.write(data)
        seen[slug] = url
        total += len(data)
        print(f"  {slug:48} {len(data) / 1024:6.1f} KB  weight {weight}")
    out_blocks.append(re.sub(r"url\(https://[^)]+\)", f"url('/fonts/{slug}')", block))

header = (
    "/*\n"
    " * Self-hosted webfonts - no runtime dependency on fonts.googleapis.com.\n"
    " *\n"
    " * Source: " + CSS_URL + "\n"
    " * Variable fonts (weight ranges), subsets: " + ", ".join(sorted(KEEP_SUBSETS)) + ".\n"
    " * Nunito Sans and Fira Code are licensed under the SIL Open Font License 1.1.\n"
    " * Re-run the fetch script (see AGENTS.md) to refresh them.\n"
    " */\n\n"
)
with open(OUT_CSS, "w") as fh:
    fh.write(header + "\n\n".join(out_blocks) + "\n")

print(f"\n{len(seen)} files ({total / 1024:.0f} KB) -> {FONT_DIR}")
print(f"{len(out_blocks)} @font-face blocks -> {OUT_CSS}")
