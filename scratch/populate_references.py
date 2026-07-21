import os
import shutil
import glob

brain_dir = r"C:\Users\ASUA\.gemini\antigravity\brain\840572dc-acb1-4fff-884b-f91f4aa92542"
workspace_dir = r"C:\Users\ASUA\.gemini\antigravity\scratch\ai-governance-control-tower"
ref_dir = os.path.join(workspace_dir, "references")

os.makedirs(ref_dir, exist_ok=True)

# Copy all .docx files from brain into references/
docx_files = glob.glob(os.path.join(brain_dir, "*.docx"))
for f in docx_files:
    filename = os.path.basename(f)
    dest = os.path.join(ref_dir, filename)
    shutil.copy(f, dest)
    print(f"Copied Word document to references/: {filename}")

# Copy key architecture and screenshots into references/
images_to_copy = [
    "hld_architecture_light_theme.png",
    "hld_architecture_diagram.png",
    "lld_architecture_diagram.png",
    "module2_compliance_auditor.png",
    "production_realtime_system.png",
    "app_rules.png",
    "app_compliance.png",
    "app_grounding.png",
    "app_audit.png",
    "app_dashboard.png",
    "app_agentic.png"
]

for img_name in images_to_copy:
    src_path = os.path.join(brain_dir, img_name)
    if os.path.exists(src_path):
        dest_path = os.path.join(ref_dir, img_name)
        shutil.copy(src_path, dest_path)
        print(f"Copied image to references/: {img_name}")

print("Populated references/ folder successfully.")
