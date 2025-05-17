from flask import Flask,redirect,url_for,render_template,request, jsonify,session
from chatterbot import ChatBot
from xuLyInput import getCauTraLoi
app = Flask(__name__)
app.secret_key = "ban_co_the_doi_chuoi_nay"

@app.route("/")
def home():
    if 'danhSachChat' not in session:
        session['danhSachChat'] = []
        # Gửi lời chào đầu tiên
        session['danhSachChat'].append({'cautraloi': 'Xin chào đến với chatuth'})
    return render_template("chatboxuth.html", danhSachChat=session['danhSachChat'])

@app.route("/get", methods=["GET"])
def chatboxuth():
    userText = request.args.get("msg")
    if userText:
        botReply = getCauTraLoi(userText)
        # Lấy danh sách chat hiện tại
        danhSach = session.get('danhSachChat', [])
        # Thêm câu hỏi và trả lời
        danhSach.append({'cauhoi': userText, 
                         'cautraloi': botReply})
        session['danhSachChat'] = danhSach
        return jsonify({"response": botReply})
    return jsonify({"response": "Không nhận được câu hỏi."})

if __name__=="__main__":
    app.run(debug=True)