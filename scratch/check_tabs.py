import re

with open('index.html', encoding='utf-8') as f:
    html = f.read()

tabs = re.findall(r'data-tab="([^"]+)"', html)
panels = re.findall(r'id="(tab-[^"]+)"', html)

print("Nav Button Tabs:", tabs)
print("Tab Panel IDs:", panels)

# Check mismatches
for t in tabs:
    expected_id = f"tab-{t}"
    if expected_id not in panels:
        print(f"MISMATCH! Nav tab '{t}' expects panel ID '{expected_id}', but '{expected_id}' is NOT found in index.html!")
    else:
        print(f"MATCH: Nav tab '{t}' -> Panel ID '{expected_id}' OK")
