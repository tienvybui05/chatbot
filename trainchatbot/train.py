from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
chatbot = ChatBot(
    "Chatbot",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///databasebot.sqlite3',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Xin lỗi, tôi không hiểu.'
        }
    ]
)


trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("vietnamese/gioithieu.yml")
list_trainer = ListTrainer(chatbot)
trainer = ListTrainer(chatbot)
print("Train thành công! Bắt đầu trò chuyện...")