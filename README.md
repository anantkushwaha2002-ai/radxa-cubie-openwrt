# Radxa Cubie A5E OpenWrt 24.10 by Anant Kushwaha

[![Firmware Version](https://img.shields.io/badge/OpenWrt-24.10.0-blue.svg)](https://openwrt.org/)
[![Hardware](https://img.shields.io/badge/Hardware-Radxa%20Cubie%20A5E-orange.svg)](https://radxa.com/)
[![Maintainer](https://img.shields.io/badge/Maintainer-Anant%20Kushwaha-green.svg)](https://github.com/anantkushwaha2002-ai)
[![License](https://img.shields.io/badge/License-GPL--2.0-yellow.svg)](LICENSE)

An optimized, clean, and fully localized OpenWrt firmware image for the **Radxa Cubie A5E** (Allwinner sun55iw3 / A523 Octa-Core ARM64). Pre-configured with **Docker engine**, **Captive Portal support**, and an intuitive **Real-Time QuickStart Dashboard** designed by **Anant Kushwaha**.

---

## 🚀 Key Features

* **Custom Real-Time QuickStart Home Dashboard**:
  * Real-time network bandwidth graph (Up/Down speed curve).
  * Live Ethernet port indicators (WAN / LAN status, link speeds).
  * System Information (CPU usage, RAM allocation, CPU temperature).
  * Mounted storage devices overview.
  * RAM Release & system tools directly from LuCI.
* **100% Cleaned & Unbloated**:
  * Removed foreign links, Chinese cloud dependencies, and unwanted Chinese mirrors.
  * Direct official OpenWrt package feeds (`downloads.openwrt.org`).
  * Default LuCI language set strictly to English (`en`).
* **RAM & Swap Stability Protection**:
  * Pre-configured **1 GB high-speed Swap partition** (`/mnt/storage/swapfile`) prevents Out-Of-Memory (OOM) crashes even under high Docker workload.
  * Memory compaction & cache cleanup script (`ram_release.sh`) configured for **Indian Standard Time (`Asia/Kolkata`)**.
* **Docker & Container Ready**:
  * Docker Engine pre-installed and verified with multiple microservices (Node.js, MariaDB, Apache2, FreeRADIUS, Cloudflare Tunnel).
* **Network & Offloading Performance**:
  * Dual Gigabit Ethernet optimization.
  * GRO offloading tuned for captive portal billing stability.

---

## 📋 Hardware Specifications

| Component | Specification |
| :--- | :--- |
| **SoC** | Allwinner sun55iw3 / A523 (8x Cortex-A55 @ 1.8 GHz) |
| **Architecture** | ARM64 (`aarch64_generic` / `armsr/armv8`) |
| **Kernel** | Linux 5.15.147-cubieA5E |
| **RAM** | 1GB / 2GB / 4GB LPDDR4X (with +1GB Swap) |
| **Boot Media** | MicroSD Card |
| **Ethernet** | 2x Gigabit LAN / WAN |

---

## 📥 Download Firmware

The ready-to-flash firmware archive is hosted on **GitHub Releases**:

👉 **[Download OpenWrt 24.10 by Anant Kushwaha (.zip / 331 MB)](https://github.com/anantkushwaha2002-ai/radxa-cubie-openwrt/releases/download/v1.0.0/radxa_cubie_a5e_openwrt_24.10_by_anant_kushwaha.zip)**

*(Contains the uncompressed flashable `radxa_cubie_a5e_clean_openwrt_docker.img` file ~660 MB)*

---

## 🛠️ Installation & Flashing Guide

1. Download the latest `.img` from the Releases section.
2. Insert a high-speed MicroSD card (Class 10 / A1 or A2 recommended, at least 8 GB).
3. Use **Balena Etcher**, **Rufus**, or **PhoenixCard** to flash the `.img` onto your SD card.
4. Insert the SD card into your **Radxa Cubie A5E** and power on the board.
5. Connect your PC to the LAN Ethernet port.

### Default Access Credentials
* **Router IP**: `192.168.10.1`
* **Web UI (LuCI)**: `https://192.168.10.1/`
* **SSH**: `ssh root@192.168.10.1`
* **Username**: `root`
* **Password**: *No password by default (set your password upon first login)*

---

## 🔧 Building & Modifying from Source

If you want to customize this firmware, modify dashboard components, or recompile packages:

### Prerequisites
* Windows 10/11 or Linux
* Python 3.10+
* Git

### Step-by-Step Build:
1. Clone the repository:
   ```bash
   git clone https://github.com/anantkushwaha2002-ai/radxa-cubie-openwrt.git
   cd radxa-cubie-openwrt
   ```

2. Make your modifications:
   * **LuCI Frontend / Views**: edit files in `quickstart_payload/www/luci-static/quickstart/`
   * **Backend Controllers / Daemons**: edit `quickstart_payload/usr/lib/lua/luci/controller/` and `quickstart_payload/usr/sbin/`
   * **Configs & Scripts**: edit `configs/` and `quickstart_payload/etc/`

3. Rebuild the firmware:
   ```bash
   python build.py
   ```
   The script will automatically inject changes into rootfs, convert to sparse format, recalculate the 32-bit Allwinner verification checksum, and pack the `.img` via `imgRePacker`.

---

## 👤 Author & Credits

* **Firmware Customization & Build**: **Anant Kushwaha**
* **Upstream**: [OpenWrt Project](https://openwrt.org/) & [Radxa](https://radxa.com/)

