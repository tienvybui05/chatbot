import sqlite3

def xem_cau_hoi_chua_tra_loi():
    """Truy vấn và hiển thị các câu hỏi chưa có câu trả lời."""
    conn = sqlite3.connect('trainchatbot/databasebot.sqlite3')
    cursor = conn.cursor()

    # Truy vấn tất cả các câu hỏi chưa có câu trả lời
    cursor.execute('SELECT id, question, timestamp FROM unanswered_questions')
    unanswered_questions = cursor.fetchall()

    if unanswered_questions:
        print("Danh sách câu hỏi chưa có câu trả lời:")
        for question in unanswered_questions:
            print(f"- ID: {question[0]}, Câu hỏi: {question[1]}, Thời gian: {question[2]}")
    else:
        print("Hiện tại không có câu hỏi nào chưa được trả lời.")

    conn.close()

if __name__ == "__main__":
    xem_cau_hoi_chua_tra_loi()