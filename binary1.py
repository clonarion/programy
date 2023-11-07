try:
    with open(r"C:/Users/matto/OneDrive/Dokumenty/ja som textovy dokument.txt", 'rb') as file:
        for offset, data in enumerate(iter(lambda: file.read(16), b''), 1):
            hex_data = ' '.join(f'{byte:02X}' for byte in data)
            text_data = ''.join(chr(byte) if 31 < byte < 127 else '.' for byte in data)
            print(f'{offset:08X}: {hex_data}  {text_data}')

except FileNotFoundError:
    print("File not found.")
