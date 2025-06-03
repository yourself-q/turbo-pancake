"""
メインモジュール
全てのコンポーネントを統合し、エンドツーエンドの処理フローを実行
"""

import os
import sys

# 親ディレクトリをパスに追加してモジュールをインポートできるようにする
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from src.message_processing import extract_name
from src.user_file_management import (
    get_user_file_path,
    file_exists,
    create_new_user_file,
    load_user_data
)
from src.response_generation import generate_response
from src.summary_module import summarize_conversation, save_summary

def process_message(message: str) -> str:
    """
    メッセージを処理し、応答を生成

    Args:
        message (str): ユーザーのメッセージ

    Returns:
        str: 生成されたレスポンス
    """
    # 1. 名前の推定
    name_result = extract_name(message)
    print(f"名前推定結果: {name_result}")

    if "%*name," in name_result:
        name_tag_start = name_result.find("%*name,") + len("%*name,")
        name_tag_end = name_result.find("*", name_tag_start)
        user_name = name_result[name_tag_start:name_tag_end]
    else:
        user_name = "unknown"

    # 2. ファイルの確認
    file_path = get_user_file_path(user_name)
    if file_exists(file_path):
        print(f"ユーザーファイルが存在します: {file_path}")
        user_data = load_user_data(file_path)
        file_status = "%*file,exists*%"
    else:
        print(f"新規ユーザーです。ファイルを作成します: {file_path}")
        create_new_user_file(file_path, "")
        user_data = ""
        file_status = "%*file,new*%"

    # 3. レスポンス生成
    response = generate_response(user_name, user_data, message)

    # 4. 情報要約（会話終了時に実行）
    # ここではダミーの実装として、メッセージを要約して保存
    summary = summarize_conversation(f"ユーザー: {message}\nシステム: {response}")
    save_summary(file_path, summary)

    return f"{name_result}\n{file_status}\n{response}"

# テスト用の関数
if __name__ == "__main__":
    test_messages = [
        "川合です。好きな色は赤色です。",
        "吉田です。さっきの話を続けましょう。",
        "さっき話した内容覚えてる？"
    ]

    for msg in test_messages:
        print(f"\n=== テストメッセージ: {msg} ===")
        response = process_message(msg)
        print(f"レスポンス:\n{response}")