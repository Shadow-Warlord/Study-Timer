"""Runs in CI after `npx cap add android`.
Lets the app draw into the display-cutout area (edge to edge); the page keeps its content clear of it via CSS safe-area insets."""
import pathlib, sys
p = pathlib.Path("android/app/src/main/res/values/styles.xml")
s = p.read_text(encoding="utf-8")
item = '        <item name="android:windowLayoutInDisplayCutoutMode">shortEdges</item>\n'
for anchor in ('        <item name="android:background">@null</item>\n',
               '        <item name="android:background">@drawable/splash</item>\n'):
    if anchor not in s:
        sys.exit("styles.xml anchor not found: " + anchor.strip())
    s = s.replace(anchor, anchor + item)
p.write_text(s, encoding="utf-8")
print("patched", p)
