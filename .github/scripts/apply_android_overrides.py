#!/usr/bin/env python3
"""Apply MR Store's custom splash screen to the generated Capacitor Android project.

Run from the repository root AFTER `npx cap add android` and `npx capacitor-assets generate`.
 - copies android-overrides/res/** into android/app/src/main/res/
 - points the launch theme at the MR Store background colour + splash logo
 - hides the WebView's native scrollbars (the CSS alone can't hide the page scrollbar)
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

# 3) hide the native WebView scrollbars (the thin bar on the right while scrolling)
JAVA_ROOT = ROOT / "android" / "app" / "src" / "main" / "java"
activities = list(JAVA_ROOT.rglob("MainActivity.java"))
if len(activities) != 1:
    sys.exit(f"ERROR: expected exactly one MainActivity.java under {JAVA_ROOT}, found {len(activities)}")
main = activities[0]
java = main.read_text(encoding="utf-8")

if "setVerticalScrollBarEnabled" not in java:
    cls = re.search(r"(class\s+MainActivity\s+extends\s+BridgeActivity\s*\{)", java)
    if not cls:
        sys.exit("ERROR: 'class MainActivity extends BridgeActivity' not found in MainActivity.java")
    if re.search(r"void\s+onCreate\s*\(", java):
        sys.exit("ERROR: MainActivity already defines onCreate; patch it manually")

    method = """
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        WebView webView = getBridge().getWebView();
        webView.setVerticalScrollBarEnabled(false);
        webView.setHorizontalScrollBarEnabled(false);
    }
"""
    java = java[: cls.end()] + method + java[cls.end():]

    imports = ""
    for imp in ("android.os.Bundle", "android.webkit.WebView"):
        if f"import {imp};" not in java:
            imports += f"import {imp};\n"
    pkg = re.search(r"^package\s+[\w.]+;\s*$", java, re.M)
    if not pkg:
        sys.exit("ERROR: package line not found in MainActivity.java")
    java = java[: pkg.end()] + "\n\n" + imports.rstrip("\n") + java[pkg.end():]
    main.write_text(java, encoding="utf-8")
print("patched", main.relative_to(ROOT))
