import json

def read_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)  # Đọc dữ liệu JSON vào biến data
        return data
    except Exception as e:
        print(f"Lỗi khi đọc file JSON: {e}")
        return None

def main():
    file_path = 'data/output.json'  # Đường dẫn tới file JSON
    data = read_json_file(file_path)

    if data:
        print("Dữ liệu trong file JSON:")
        print(data)  # In dữ liệu ra màn hình
    else:
        print("Không đọc được dữ liệu hoặc file rỗng.")

if __name__ == "__main__":
    main()
