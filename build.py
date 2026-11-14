"""
Radxa Cubie A5E Firmware Build & Packaging Tool
Author: Anant Kushwaha
License: GPL-2.0 / MIT

Usage:
    python build.py
"""
import subprocess
import os
import sys

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")

def run_step(name, cmd):
    print(f"\n==========================================")
    print(f"[*] Step: {name}")
    print(f"==========================================")
    res = subprocess.run([sys.executable, cmd], cwd=BASE_DIR)
    if res.returncode != 0:
        print(f"[!] Error in step {name}! Code: {res.returncode}")
        sys.exit(res.returncode)

def main():
    print("Starting Radxa Cubie A5E Clean OpenWrt Firmware Build...")
    
    # Step 1: Inject payload into rootfs ISO
    run_step("1. Inject Payload into Rootfs", os.path.join(SCRIPTS_DIR, "write_all_payload_to_iso.py"))
    
    # Step 2: Convert to Sparse
    run_step("2. Convert Rootfs to Sparse Image", os.path.join(SCRIPTS_DIR, "convert_rootfs_to_sparse.py"))
    
    # Step 3: Update 32-bit Allwinner Checksum
    run_step("3. Update Allwinner Checksum", os.path.join(SCRIPTS_DIR, "update_vrootfs.py"))
    
    # Step 4: Repack with imgRePacker
    imgrepacker = os.path.join(BASE_DIR, "tools", "tools_imgrepacker", "imgRePacker.exe")
    dump_dir = os.path.join(BASE_DIR, "firmware_dump", "radxa_a5e_a527_kwrt_unofficial_sdcard_rev4.img.dump")
    if os.path.exists(dump_dir) and os.path.exists(imgrepacker):
        print(f"\n[*] Repacking with imgRePacker...")
        res = subprocess.run([imgrepacker, "/2k", dump_dir])
        if res.returncode == 0:
            print("\n[+] Firmware image created successfully!")
    else:
        print("\n[*] Rootfs and sparse images prepared. Ready for repacking.")

if __name__ == "__main__":
    main()
