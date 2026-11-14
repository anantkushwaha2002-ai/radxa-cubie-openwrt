import struct, os, time

rootfs_path = r'cubie_firmware\radxa_a5e_a527_kwrt_unofficial_sdcard_rev4.img.dump\rootfs.fex'
vrootfs_path = r'cubie_firmware\radxa_a5e_a527_kwrt_unofficial_sdcard_rev4.img.dump\Vrootfs.fex'

print(f"Calculating Allwinner 32-bit checksum for {rootfs_path}...")
sz = os.path.getsize(rootfs_path)
s = 0
chunk_size = 16 * 1024 * 1024 # 16 MB buffer

with open(rootfs_path, 'rb') as f:
    while True:
        buf = f.read(chunk_size)
        if not buf:
            break
        # Process 4-byte chunks
        rem = len(buf) % 4
        if rem != 0:
            buf = buf + b'\x00' * (4 - rem)
        # Use memoryview with struct or sum ints
        # fast unpack
        count = len(buf) // 4
        ints = struct.unpack(f'<{count}I', buf)
        s = (s + sum(ints)) & 0xFFFFFFFF

print(f"Checksum calculated: {hex(s)}")
with open(vrootfs_path, 'wb') as f:
    f.write(struct.pack('<I', s))

print(f"Updated {vrootfs_path} with {hex(s)} successfully!")

