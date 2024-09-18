import requests

# Đường dẫn API
url = "http://localhost:9001/api/v1/books"

# Hàm để tạo một bản ghi sách mới
def create_book(name, author, is_ready):
    return {
        "name": name,
        "author": author,
        "isReady": is_ready
    }

# Danh sách tên sách và tác giả Việt Nam
book_names = [
    "Tôi thấy hoa vàng trên cỏ xanh", "Nhà giả kim", "Số đỏ", "Vợ chồng A Phủ",
    "Đất rừng phương Nam", "Mắt biếc", "Truyện Kiều", "Chí Phèo", 
    "Dế Mèn phiêu lưu ký", "Lão Hạc", "Người lái đò sông Đà", 
    "Rừng xà nu", "Chiếc thuyền ngoài xa", "Vợ nhặt", "Người con gái Nam Xương",
    "Những người khốn khổ", "Tắt đèn", "Giông tố", "Đời thừa", 
    "Nỗi buồn chiến tranh", "Cánh đồng bất tận", "Nếp nhà", "Nhật ký trong tù",
    "Việt Bắc", "Con đường đau khổ", "Người mẹ cầm súng", 
    "Về miền gió cát", "Hòn Đất", "Chiến tranh và hòa bình", 
    "Sống mãi với thủ đô", "Đất nước đứng lên", "Đường cách mệnh", 
    "Gió lạnh đầu mùa", "Tắt đèn", "Tuổi thơ dữ dội", 
    "Vũ Trung tùy bút", "Số đỏ", "Thời xa vắng", "Đôi mắt"
]

authors = [
    "Nguyễn Nhật Ánh", "Paulo Coelho", "Vũ Trọng Phụng", "Tô Hoài",
    "Đoàn Giỏi", "Nguyễn Nhật Ánh", "Nguyễn Du", "Nam Cao",
    "Tô Hoài", "Nam Cao", "Nguyễn Tuân", 
    "Nguyễn Trung Thành", "Nguyễn Minh Châu", "Kim Lân", "Nguyễn Dữ",
    "Victor Hugo", "Ngô Tất Tố", "Vũ Trọng Phụng", "Nam Cao", 
    "Bảo Ninh", "Nguyễn Ngọc Tư", "Nguyễn Khắc Phê", "Hồ Chí Minh",
    "Tố Hữu", "A. Tolstoy", "Nguyễn Thi", 
    "Xuân Diệu", "Anh Đức", "Lev Tolstoy", 
    "Nguyễn Huy Tưởng", "Nguyễn Ngọc", "Nguyễn Ái Quốc", 
    "Thạch Lam", "Ngô Tất Tố", "Phùng Quán", 
    "Phạm Đình Hổ", "Vũ Trọng Phụng", "Lê Lựu", "Nam Cao"
]

def add_books_to_api():
    # Tạo dữ liệu cho từng sách với tác giả
    books = [
        create_book(book_names[i], authors[i], i % 2 == 0)
        for i in range(len(book_names))
    ]

    # Gửi từng bản ghi lên API
    for book in books:
        try:
            response = requests.post(url, json=book)
            response.raise_for_status()
            print(f"Thêm thành công: {book['name']} - Tác giả: {book['author']}")
        except requests.exceptions.RequestException as e:
            print(f"Lỗi khi thêm: {book['name']} - Tác giả: {book['author']} - Lỗi: {str(e)}")

if __name__ == "__main__":
    add_books_to_api()
