file_path = r"C:/Users/matto/OneDrive/Dokumenty/ja som textovy dokument.txt" 

try:
    with open(file_path, 'rb') as file:
        data = file.read()
        byte_value = input("enter a byte value (0-255): ")

        if byte_value.isdigit() and 0 <= (byte := int(byte_value)) <= 255:
            print(f"number of occurences of byte {byte} in the file: {data.count(byte)}")
        else:
            print("wrong input. enter a valid integer between 0 and 255.")
except FileNotFoundError:
    print("File not found.")