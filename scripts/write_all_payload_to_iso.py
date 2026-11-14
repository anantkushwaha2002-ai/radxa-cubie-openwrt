import subprocess
import os

iso_path = os.path.abspath("cubie_firmware/rootfs.fex.iso")
debugfs = os.path.abspath("tools_debugfs/debugfs.exe")
e2fsck = os.path.abspath("tools_debugfs/e2fsck.exe")
payload_dir = os.path.abspath("quickstart_payload")

# 1. Directories
dirs = [
    "/etc/config",
    "/etc/init.d",
    "/etc/rc.d",
    "/etc/hotplug.d/iface",
    "/etc/hotplug.d/block",
    "/usr/bin",
    "/usr/sbin",
    "/usr/libexec/quickstart",
    "/usr/lib",
    "/usr/lib/lua/luci/controller",
    "/usr/lib/lua/luci/view/quickstart",
    "/usr/lib/lua/luci/i18n",
    "/usr/share/luci/menu.d",
    "/www/luci-static/quickstart",
    "/www/luci-static/quickstart/i18n"
]

cmds = []
for d in dirs:
    cmds.append(f"mkdir {d}")

# 2. Files
for root, _, files in os.walk(payload_dir):
    for file in files:
        full_src = os.path.abspath(os.path.join(root, file)).replace("\\", "/")
        rel_path = os.path.relpath(full_src, payload_dir).replace("\\", "/")
        target_path = "/" + rel_path
        target_dir = os.path.dirname(target_path).replace("\\", "/")
        target_name = os.path.basename(target_path)
        
        cmds.append(f"cd {target_dir}")
        cmds.append(f"rm {target_name}")
        cmds.append(f'write "{full_src}" {target_name}')
        
        mode = "0755" if ("/init.d/" in target_path or "/sbin/" in target_path or "/libexec/" in target_path) else "0644"
        cmds.append(f"sif {target_name} mode 010{mode[-3:]}")

# 3. Symlinks
cmds.append("cd /usr/sbin")
cmds.append("rm startdhns")
cmds.append("symlink startdhns /usr/sbin/quickstart")

cmds.append("cd /etc/rc.d")
cmds.append("rm S92quickstart")
cmds.append("symlink S92quickstart ../init.d/quickstart")
cmds.append("rm S93startdhns")
cmds.append("symlink S93startdhns ../init.d/startdhns")

# 4. Remove unwanted old wizard files from ISO
cmds.append("rm /usr/lib/lua/luci/controller/wizard.lua")
cmds.append("rm /usr/share/luci/menu.d/luci-app-wizard.json")
cmds.append("rm /etc/config/wizard")

cmd_file = "batch_iso_patch.txt"
with open(cmd_file, "w", encoding="utf-8") as f:
    for c in cmds:
        f.write(c + "\n")

print(f"Executing {len(cmds)} commands in debugfs...")
res = subprocess.run([debugfs, "-w", "-f", cmd_file, iso_path], capture_output=True, text=True)
if os.path.exists(cmd_file):
    os.remove(cmd_file)

# Run e2fsck twice
res_fsck1 = subprocess.run([e2fsck, "-y", "-f", iso_path], capture_output=True, text=True)
res_fsck2 = subprocess.run([e2fsck, "-y", "-f", iso_path], capture_output=True, text=True)

print("e2fsck pass 1 code:", res_fsck1.returncode)
print("e2fsck pass 2 code:", res_fsck2.returncode)

# Verification
verify_files = [
    "/usr/sbin/quickstart",
    "/usr/sbin/startdhns",
    "/usr/bin/ram_release.sh",
    "/etc/init.d/quickstart",
    "/etc/rc.d/S92quickstart",
    "/etc/config/luci",
    "/usr/lib/os-release",
    "/etc/os-release",
    "/usr/share/luci/menu.d/luci-app-quickstart.json",
    "/usr/lib/lua/luci/controller/quickstart.lua",
    "/usr/lib/lua/luci/controller/istore_backend.lua",
    "/www/luci-static/quickstart/index.js",
    "/www/luci-static/quickstart/vendor.js",
    "/www/luci-static/quickstart/style.css"
]

all_ok = True
for vf in verify_files:
    d = os.path.dirname(vf).replace("\\", "/")
    b = os.path.basename(vf)
    r = subprocess.run([debugfs, "-R", f"stat {vf}", iso_path], capture_output=True, text=True)
    if "File not found" in r.stdout or "Inode: 0" in r.stdout:
        print(f"[FAIL] {vf}")
        all_ok = False
    else:
        # extract size
        import re
        m = re.search(r"Size:\s+(\d+)", r.stdout)
        sz = m.group(1) if m else "ok"
        print(f"[OK] {vf} (Size: {sz})")

if all_ok:
    print("\nALL FILES VERIFIED SUCCESSFULLY IN rootfs.fex.iso!")
else:
    print("\nSOME FILES FAILED VERIFICATION!")

