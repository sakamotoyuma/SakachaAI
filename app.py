import os
import openai
from flask import Flask, render_template, request, jsonify
from search import answer_question  # search.pyからanswer_question関数をインポート

app = Flask(__name__)

openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("user_input")
    conversation_history = request.json.get("conversation_history", [])

    conversation_history = [{"role": "system", "content": "あなたはこのプログラムコードの制作者「さかちゃ」です。フレンドリーに回答してください。語尾に「！」をつけてください"}]

    # search.pyのanswer_question関数を呼び出し、回答を生成
    answer = answer_question(user_input, conversation_history)
    
    conversation_history.append({"role": "assistant", "content": answer})

    return jsonify({"response": answer, "conversation_history": conversation_history})

if __name__ == '__main__':
    app.run(debug=True)
