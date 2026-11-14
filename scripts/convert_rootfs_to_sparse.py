import struct, os, time

CHUNK_TYPE_RAW = 0xCAC1
CHUNK_TYPE_FILL = 0xCAC2
CHUNK_TYPE_DONT_CARE = 0xCAC3
SPARSE_HEADER_MAGIC = 0xED26FF3A

def raw_to_simg(raw_path, simg_path, block_size=4096):
    file_size = os.path.getsize(raw_path)
    total_blocks = (file_size + block_size - 1) // block_size
    print(f"Converting {raw_path} ({file_size} bytes, {total_blocks} blocks) -> {simg_path}...")
    
    start_time = time.time()
    chunks = 0
    with open(raw_path, 'rb') as raw_f, open(simg_path, 'wb') as simg_f:
        simg_f.seek(28)
        
        current_type = None
        current_blocks = 0
        current_data = bytearray()
        
        def flush_chunk():
            nonlocal chunks, current_type, current_blocks, current_data
            if current_blocks == 0:
                return
            if current_type == 'dont_care':
                hdr = struct.pack('<2H2I', CHUNK_TYPE_DONT_CARE, 0, current_blocks, 12)
                simg_f.write(hdr)
            elif current_type == 'raw':
                total_sz = 12 + len(current_data)
                hdr = struct.pack('<2H2I', CHUNK_TYPE_RAW, 0, current_blocks, total_sz)
                simg_f.write(hdr)
                simg_f.write(current_data)
            chunks += 1
            current_type = None
            current_blocks = 0
            current_data = bytearray()
            
        empty_block = b'\x00' * block_size
        
        # Read in large chunks (64 MB buffer) for fast Windows disk I/O
        READ_CHUNK_SIZE = 64 * 1024 * 1024
        processed_blocks = 0
        last_report = time.time()
        
        while True:
            big_buf = raw_f.read(READ_CHUNK_SIZE)
            if not big_buf:
                break
                
            num_in_buf = (len(big_buf) + block_size - 1) // block_size
            for i in range(0, len(big_buf), block_size):
                buf = big_buf[i:i+block_size]
                if len(buf) < block_size:
                    buf = buf.ljust(block_size, b'\x00')
                    
                is_empty = (buf == empty_block)
                btype = 'dont_care' if is_empty else 'raw'
                
                if current_type == btype and (current_blocks < 65535) and (len(current_data) + block_size <= 64 * 1024 * 1024):
                    current_blocks += 1
                    if btype == 'raw':
                        current_data.extend(buf)
                else:
                    flush_chunk()
                    current_type = btype
                    current_blocks = 1
                    if btype == 'raw':
                        current_data.extend(buf)
                        
                processed_blocks += 1
                
            if time.time() - last_report > 5:
                pct = (processed_blocks / total_blocks) * 100
                print(f"Progress: {processed_blocks}/{total_blocks} blocks ({pct:.1f}%) in {time.time() - start_time:.1f}s")
                last_report = time.time()
                
        flush_chunk()
        
        # Write real header at offset 0
        simg_f.seek(0)
        fhdr = struct.pack('<I4H4I', SPARSE_HEADER_MAGIC, 1, 0, 28, 12, block_size, total_blocks, chunks, 0)
        simg_f.write(fhdr)
        
    elapsed = time.time() - start_time
    simg_sz = os.path.getsize(simg_path)
    print(f"Successfully converted in {elapsed:.1f}s! Sparse size: {simg_sz / (1024*1024):.2f} MB, {chunks} chunks.")

if __name__ == '__main__':
    raw_path = r'cubie_firmware\rootfs.fex.iso'
    simg_path = r'cubie_firmware\radxa_a5e_a527_kwrt_unofficial_sdcard_rev4.img.dump\rootfs.fex'
    raw_to_simg(raw_path, simg_path)

