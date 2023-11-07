try:
    with open(r"C:/Users/matto/OneDrive/Dokumenty/ja som textovy dokument.txt", 'rb') as file:
        data = file.read()
        if len(data) < 10:
            print("not enough bytes.")
        else:
            middle_start = max(len(data) // 2 - 5, 0)
            print(f"first 10 bytes: {data[:10]}")
            print(f"last 10 bytes: {data[-10:]}")
            print(f"10 bytes around the middle: {data[middle_start:middle_start + 10]}")
except FileNotFoundError:
    print("File not found.")
