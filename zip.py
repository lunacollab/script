import zipfile
import io

original_zip_file_path = ""
new_zip_file_path = ""

def replace_in_content(content, old_str, new_str):
    return content.replace(old_str, new_str)

def replace_in_path(path, old_str, new_str):
    return path.replace(old_str, new_str)

buffer = io.BytesIO()

with zipfile.ZipFile(original_zip_file_path, 'r') as zip_ref:
    with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as new_zip_ref:
        zip_items = zip_ref.namelist()
        
        for item in zip_items:
            new_item = replace_in_path(item, "a", "example")
            
            data = zip_ref.read(item)
            
            try:
                data_str = data.decode('utf-8')
                data_str = replace_in_content(data_str, "a", "example")
                data = data_str.encode('utf-8')
            except UnicodeDecodeError:
                pass
            
            new_zip_ref.writestr(new_item, data)

with open(new_zip_file_path, 'wb') as f:
    f.write(buffer.getvalue())

print(f'Đã tạo tệp zip mới tại: {new_zip_file_path}')
