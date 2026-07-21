import subprocess
import os

tabs = ['dashboard', 'security', 'policy', 'explainability', 'compliance', 'agentic']
img_dir = r"C:\Users\ASUA\.gemini\antigravity\brain\840572dc-acb1-4fff-884b-f91f4aa92542"

print("Testing all web browser tabs on http://localhost:8081/...")
for t in tabs:
    out_file = os.path.join(img_dir, f"browser_test_{t}.png")
    cmd = f'start-process msedge -ArgumentList "--headless", "--disable-gpu", "--window-size=1600,1000", "--screenshot={out_file}", "http://localhost:8081/?tab={t}" -Wait'
    subprocess.run(["powershell", "-Command", cmd], capture_output=True)
    
    if os.path.exists(out_file) and os.path.getsize(out_file) > 10000:
        print(f"  [SUCCESS] Tab '{t}' rendered screenshot: {os.path.basename(out_file)} ({os.path.getsize(out_file)} bytes)")
    else:
        print(f"  [FAILURE] Tab '{t}' failed to render screenshot!")
