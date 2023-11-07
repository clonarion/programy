import os

folder_path = r"C:\Users\matto\OneDrive\Dokumenty\abeceda"

file_signatures = {
    "PNG": {
        "signature": bytes.fromhex("89504E470D0A1A0A"),
        "offset": 0,
        "length": 8
    },
    "JPEG": {
        "signature": bytes.fromhex("FFD8"),
        "offset": 0,
        "length": 2
    },
    "GIF": {
        "signature": bytes.fromhex("474946383961"),
        "offset": 0,
        "length": 6
    },
    "PDF": {
        "signature": bytes.fromhex("25504446"),
        "offset": 0,
        "length": 4
    },
    "ZIP": {
        "signature": bytes.fromhex("504B0304"),
        "offset": 0,
        "length": 4
    },
    "DOCX": {
        "signature": bytes.fromhex("504B030414000600"),
        "offset": 0,
        "length": 8
    },
    "BMP": {
        "signature": bytes.fromhex("424D"),
        "offset": 0,
        "length": 2
    },
    "MP3": {
        "signature": bytes.fromhex("494433"),
        "offset": 0,
        "length": 3
    },
    "AVI": {
        "signature": bytes.fromhex("52494646"),
        "offset": 0,
        "length": 4
    },
    "MP4": {
        "signature": bytes.fromhex("66747970"),
        "offset": 4,
        "length": 4
    },
    "TXT": {
        "signature": b"HelloTxt",
        "offset": 0,
        "length": 8
    },
    "HTML": {
        "signature": b"<!DOCTYPE",
        "offset": 0,
        "length": 9
    },
    "CSV": {
        "signature": b",,,",
        "offset": 0,
        "length": 3
    },
    "XML": {
        "signature": b"<?xml",
        "offset": 0,
        "length": 5
    },
    "JPG": {
        "signature": bytes.fromhex("FFD9"),
        "offset": -2,
        "length": 2
    },
    "EXE": {
        "signature": b"MZ",
        "offset": 0,
        "length": 2
    },
    "DLL": {
        "signature": b"MZ",
        "offset": 0,
        "length": 2
    },
    "JSON": {
        "signature": b"{\"json\":",
        "offset": 0,
        "length": 8
    }
}

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    
    if os.path.isfile(file_path):
        with open(file_path, 'rb') as file:
            data = file.read()

        for file_type, config in file_signatures.items():
            signature = config["signature"]
            offset = config["offset"]
            length = config["length"]

            if len(data) >= abs(offset) + length and data[offset:offset + length] == signature:
                print(f"File type: {file_type} - {filename}")
                break
        else:
            print(f"unknown - {filename}")