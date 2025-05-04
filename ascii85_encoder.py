import sys

def ascii85_encode(data: bytes) -> str:
    result = []
    padding = (4 - len(data) % 4) % 4
    data += b'\0' * padding

    for i in range(0, len(data), 4):
        chunk = data[i:i+4]
        num = int.from_bytes(chunk, 'big')

        if num == 0:
            result.append('z')
            continue

        block = ''
        for _ in range(5):
            num, rem = divmod(num, 85)
            block = chr(rem + 33) + block
        result.append(block)

    if padding:
        result[-1] = result[-1][:5 - padding]

    return ''.join(result)

def read_gradually():
    for line in sys.stdin:
        line = line.rstrip("\n")
        encoded_line = ascii85_encode(line.encode())
        sys.stdout.write(encoded_line + "\n")
        sys.stdout.flush()

def read_all_at_once():
    data = sys.stdin.read()
    if not data.strip():
        sys.stderr.write("Error: No input received.\n")
        sys.exit(1)

    encoded_data = ascii85_encode(data.encode())
    sys.stdout.write(encoded_data + "\n")

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
