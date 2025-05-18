import sys

def ascii85_encode(data: bytes) -> bytes:
    result = bytearray()
    padding = (4 - len(data) % 4) % 4
    data += b'\0' * padding

    for i in range(0, len(data), 4):
        chunk = data[i:i+4]
        num = int.from_bytes(chunk, 'big')

        if num == 0:
            result.extend(b'z')
            continue

        block = bytearray(5)
        for j in range(4, -1, -1):
            num, rem = divmod(num, 85)
            block[j] = rem + 33
        result.extend(block)

    if padding:
        result = result[:-padding]

    return bytes(result)

def read_gradually():
    while True:
        chunk = sys.stdin.buffer.read(4096)
        if not chunk:
            break
        encoded = ascii85_encode(chunk)
        sys.stdout.buffer.write(encoded)
        sys.stdout.buffer.flush()

def read_all_at_once():
    data = sys.stdin.buffer.read()
    if not data:
        sys.stderr.write("Error: No input received.\n")
        sys.exit(1)

    encoded = ascii85_encode(data)
    sys.stdout.buffer.write(encoded)
    sys.stdout.buffer.flush()

def main():
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: python ascii85_encoder.py [gradual|all-at-once]\n")
        sys.exit(1)

    mode = sys.argv[1]

    if mode == "gradual":
        read_gradually()
    elif mode == "all-at-once":
        read_all_at_once()
    else:
        sys.stderr.write("Invalid mode. Use 'gradual' or 'all-at-once'.\n")
        sys.exit(1)

if __name__ == "__main__":
    main()

    
