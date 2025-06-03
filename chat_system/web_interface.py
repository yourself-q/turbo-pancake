"""
ウェブインターフェース
チャットシステムの簡単なウェブインターフェースを提供
"""

import os
import sys

# 親ディレクトリをパスに追加してモジュールをインポートできるようにする
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from flask import Flask, request, jsonify, render_template_string
from src.main import process_message as main_module_process_message

app = Flask(__name__)

# HTMLテンプレート
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title>チャットシステム</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        #chat-box { width: 100%; height: 400px; border: 1px solid #ccc; padding: 10px; overflow-y: scroll; }
        .message { margin-bottom: 10px; }
        .user-message { text-align: right; color: blue; }
        .system-message { text-align: left; color: green; }
    </style>
</head>
<body>
    <h1>LMSTUDIOを用いたユーザー情報記録・管理システム</h1>
    <div id="chat-box">
        {% for message in messages %}
            <div class="message {{ 'user-message' if message['type'] == 'user' else 'system-message' }}">
                {{ message['text'] }}
            </div>
        {% endfor %}
    </div>
    <form id="chat-form" method="post">
        <input type="text" name="message" placeholder="メッセージを入力してください" required>
        <button type="submit">送信</button>
    </form>

    <script>
        document.getElementById('chat-form').onsubmit = function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            fetch('/', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                // Update chat box with new message
                const chatBox = document.getElementById('chat-box');
                chatBox.innerHTML += `
                    <div class="message user-message">${formData.get('message')}</div>
                    <div class="message system-message">${data.response}</div>
                `;
                // Scroll to bottom
                chatBox.scrollTop = chatBox.scrollHeight;
            });
        }
    </script>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_message = request.form['message']
        response = main_module_process_message(user_message)
        return jsonify({'response': response})

    # For initial GET request, render empty chat
    return render_template_string(HTML_TEMPLATE, messages=[])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=54830, debug=True)