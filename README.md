# Radxa Cubie A5E OpenWrt 24.10 by Anant Kushwaha

[![Firmware Version](https://img.shields.io/badge/OpenWrt-24.10.0-blue.svg)](https://openwrt.org/)
[![Hardware](https://img.shields.io/badge/Hardware-Radxa%20Cubie%20A5E-orange.svg)](https://radxa.com/)
[![Compatibility](https://img.shields.io/badge/RAM%20Variants-1GB%20%7C%202GB%20%7C%204GB-purple.svg)](https://radxa.com/)
[![Maintainer](https://img.shields.io/badge/Customization-Anant%20Kushwaha-green.svg)](https://github.com/anantkushwaha2002-ai)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An optimized, clean, and fully localized OpenWrt 24.10 firmware build for the **Radxa Cubie A5E** (Allwinner sun55iw3 / A523 Octa-Core ARM64). Customized and maintained by **Anant Kushwaha**.

This release is a **100% clean, blank slate** with standard OpenWrt defaults, fixed wireless networking, and a customized real-time dashboard.

---

## 📋 Hardware Specifications

<table>
<tr>
<td width="52%" valign="top">

| Component | Specification |
| :--- | :--- |
| **Target Board** | Radxa Cubie A5E |
| **Supported Variants** | 1GB, 2GB, and 4GB LPDDR4X |
| **SoC** | Allwinner sun55iw3 / A523 (8x Cortex-A55 @ 1.8 GHz) |
| **Architecture** | ARM64 (`aarch64_generic` / `armsr/armv8`) |
| **Kernel** | Linux 5.15.147-cubieA5E |
| **Wireless** | 2.4GHz & 5GHz Wi-Fi (Fixed & Verified) |
| **Ethernet** | 2x Gigabit Ethernet (eth0 LAN / eth1 WAN) |
| **Storage** | MicroSD Card Boot + High-Speed Storage (+1GB Swap) |

</td>
<td width="48%" align="center" valign="middle">

<img src="images/radxa_cubie_a5e_board.webp" alt="Radxa Cubie A5E Board Overview" width="100%" style="border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.15);" />
<br />
<em>Official Radxa Cubie A5E Single Board Computer</em>

</td>
</tr>
</table>

---

## 🚀 Key Features

* **Universal Hardware Compatibility (1GB, 2GB, 4GB RAM)**:
  * Works out-of-the-box on all three hardware variants of the **Radxa Cubie A5E (1GB, 2GB, and 4GB RAM)**.
* **Fixed Wireless (Wi-Fi) Stack**:
  * In earlier unofficial firmware images, the Wi-Fi interface was non-functional.
  * This build completely resolves the wireless subsystem (`mac80211` / AIC driver stack) for stable 2.4 GHz and 5 GHz wireless networking.
* **100% Stock & Standard OpenWrt Configurations**:
  * Pure default OpenWrt configurations for Network, LAN, WAN, DHCP, and Firewall.
  * **Completely blank & clean**: Zero private containers, zero third-party cloud services, zero bloatware. Clean and ready for your own custom setup.
* **Custom Real-Time QuickStart Dashboard**:
  * Real-time network bandwidth graph (live Up/Down speed flow curve).
  * Live physical Ethernet port indicators (WAN / LAN link states, speeds, duplex).
  * Real-time System Metrics (CPU utilization, RAM allocation, CPU temperature).
  * Storage device overview and one-click RAM release utility.
* **100% De-bloated & Localized**:
  * Stripped of foreign mirrors, Chinese telemetry, and external third-party links.
  * Configured directly to official OpenWrt package feeds (`downloads.openwrt.org`).
  * Default LuCI WebUI language set strictly to English (`en`).
* **RAM & Swap Stability Protection**:
  * Auto-configured **1 GB high-speed swap partition** protects 1GB, 2GB, and 4GB models from Out-Of-Memory (OOM) crashes under heavy router workloads.
  * Localized RAM release scheduling configured for **Indian Standard Time (`Asia/Kolkata`)**.

---

## 📥 Download Firmware & Flashing Tools

Everything needed to flash and run this firmware is available right here:

| Item | Description | Size | Download Link |
| :--- | :--- | :--- | :--- |
| **OpenWrt 24.10 Firmware (.zip)** | Ready-to-flash SD card image by Anant Kushwaha | ~331 MB | [📥 Download Firmware (.zip)](https://github.com/anantkushwaha2002-ai/radxa-cubie-openwrt/releases/download/v1.0.0/radxa_cubie_a5e_openwrt_24.10_by_anant_kushwaha.zip) |
| **PhoenixCard Tool (v4.3.1)** | Allwinner SD card burning tool for Windows | ~9.2 MB | [📥 Download PhoenixCard (v4.3.1)](https://github.com/anantkushwaha2002-ai/radxa-cubie-openwrt/releases/download/v1.0.0/PhoenixCard_V4.3.1.zip) *(or in [`tools/`](tools/PhoenixCard_V4.3.1.zip))* |

---

## 🛠️ Installation & Flashing Guide

You can flash the image using **PhoenixCard** (recommended for Allwinner SBCs) or **Balena Etcher / Rufus**:

### Method 1: Using PhoenixCard (Recommended for Allwinner)
1. Download and extract **`PhoenixCard_V4.3.1.zip`**.
2. Launch `PhoenixCard.exe`.
3. Select your MicroSD card disk from the drive dropdown list.
4. Click **Image File** and choose the extracted `radxa_cubie_a5e_openwrt_24.10_by_anant_kushwaha.img`.
5. In **Write Mode**, choose **Startup**.
6. Click **Burn** and wait until burning is complete.

### Method 2: Using Balena Etcher / Rufus
1. Open Balena Etcher or Rufus.
2. Select `radxa_cubie_a5e_openwrt_24.10_by_anant_kushwaha.img`.
3. Select your MicroSD card target and click **Flash**.

### Booting Up:
1. Insert the MicroSD card into your **Radxa Cubie A5E**.
2. Connect power (5V Type-C) and connect your PC to the LAN Ethernet port.
3. Access credentials:
   * **Web UI (LuCI)**: `https://192.168.10.1/`
   * **SSH**: `ssh root@192.168.10.1`
   * **Default Password**: *None (No password by default; set your password upon first login)*

---

## 🔧 Building & Modifying from Source

This repository contains all necessary scripts and tools so anyone can freely modify and rebuild the firmware:

### Prerequisites
* Windows 10/11 or Linux
* Python 3.10+
* Git

### Build Instructions:
1. Clone this repository:
   ```bash
   git clone https://github.com/anantkushwaha2002-ai/radxa-cubie-openwrt.git
   cd radxa-cubie-openwrt
   ```

2. Make your desired modifications:
   * **LuCI Dashboard**: modify files in `quickstart_payload/www/luci-static/quickstart/`
   * **Backend Controllers**: modify `quickstart_payload/usr/lib/lua/luci/controller/`
   * **Configurations**: modify `configs/` and `quickstart_payload/etc/`

3. Rebuild the firmware image:
   ```bash
   python build.py
   ```
   The build script will automatically inject changes into rootfs, convert to sparse image format, update the 32-bit Allwinner checksum, and repack the final `.img` file using `imgRePacker`.

---

## 👤 Author & Credits

* **Firmware Customization, Optimization & Maintenance**: **Anant Kushwaha**
* **Upstream Base**: [OpenWrt Project](https://openwrt.org/) & [Radxa](https://radxa.com/) & Kwrt Team
* **License**: Released under the permissive **[MIT License](LICENSE)** — anyone is completely free to copy, modify, distribute, and adapt this work.
