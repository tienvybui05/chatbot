from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from flask import session
import sqlite3
chatbot = ChatBot(
    "Chatbot",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///trainchatbot/databasebot.sqlite3',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Xin lỗi, tôi không hiểu.'
        }
    ]
    ,read_only = True
)
list_trainer = ListTrainer(chatbot)

def getCauTraLoi(cauHoi):
    try:
        cauTraLoi = chatbot.get_response(cauHoi)
        if cauTraLoi.confidence < 0.6:
            luu_cau_hoi_khong_tra_loi(cauHoi)
            return "Tôi không chắc về câu trả lời."
        return str(cauTraLoi)
    except:
        print("Lỗi xử lý câu trả lời từ người dùng")
def luu_cau_hoi_khong_tra_loi(cau_hoi):
    """Lưu câu hỏi không có câu trả lời vào cơ sở dữ liệu."""
    conn = sqlite3.connect('trainchatbot/databasebot.sqlite3')
    cursor = conn.cursor()

    # Tạo bảng nếu chưa tồn tại
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS unanswered_questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Thêm câu hỏi vào bảng
    cursor.execute('''
    INSERT INTO unanswered_questions (question)
    VALUES (?)
    ''', (cau_hoi,))

    conn.commit()
    conn.close()





