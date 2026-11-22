#!/usr/bin/env python3
"""Apply MR Store's custom splash screen to the generated Capacitor Android project.

Run from the repository root AFTER `npx cap add android` and `npx capacitor-assets generate`.
 - copies android-overrides/res/** into android/app/src/main/res/
 - points the launch theme at the MR Store background colour + splash logo
Fails loudly if the expected theme is not found, so a broken splash never ships silently.
"""
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "android-overrides" / "res"
DST = ROOT / "android" / "app" / "src" / "main" / "res"
STYLES = DST / "values" / "styles.xml"

if not DST.is_dir():
    sys.exit(f"ERROR: {DST} not found. Run `npx cap add android` first.")

# 1) copy resources (logo for the splash, colour)
for f in SRC.rglob("*"):
    if f.is_file():
        target = DST / f.relative_to(SRC)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(f, target)
        print("copied", f.relative_to(ROOT), "->", target.relative_to(ROOT))

# 2) patch the launch theme
xml = STYLES.read_text(encoding="utf-8")
pattern = re.compile(r'(<style\s+name="AppTheme\.NoActionBarLaunch"[^>]*>)(.*?)(</style>)', re.S)
match = pattern.search(xml)
if not match:
    sys.exit('ERROR: style "AppTheme.NoActionBarLaunch" not found in styles.xml')

items = {
    "windowSplashScreenBackground": "@color/mr_splash_background",
    "windowSplashScreenAnimatedIcon": "@drawable/mr_splash_icon",
}
body = match.group(2)
for name, value in items.items():
    line = f'<item name="{name}">{value}</item>'
    if re.search(rf'<item\s+name="{name}"', body):
        body = re.sub(rf'<item\s+name="{name}">[^<]*</item>', line, body)
    else:
        body = body.rstrip() + f"\n        {line}\n    "

xml = xml[: match.start()] + match.group(1) + body + match.group(3) + xml[match.end():]
STYLES.write_text(xml, encoding="utf-8")
print("patched", STYLES.relative_to(ROOT))
