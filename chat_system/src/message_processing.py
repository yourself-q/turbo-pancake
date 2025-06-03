"""
メッセージ処理モジュール
ユーザーからのメッセージを受け取り、名前を抽出する
"""

def extract_name(message: str) -> str:
    """
    メッセージから名前を抽出し、フォーマットで返す

    Args:
        message (str): ユーザーのメッセージ

    Returns:
        str: 名前が見つかった場合は `%*name,<name>*%` の形式
             名前が見つからない場合は `%*name,unknown*%`
    """
    # TODO: LMSTUDIOを用いて名前を抽出するロジックを実装
    # ここではダミーの実装
    if "です" in message:
        name = message.split("です")[0].strip()
        return f"%*name,{name}*%"
    else:
        return "%*name,unknown*%"
def process_message(user_message):
    import os
    name = extract_name(user_message)  # LMSTUDIOを用いて名前を抽出
    if not name:
        name = "unknown"
    user_file = f"{name}.txt"  # ユーザー名に基づくファイル名
    if os.path.exists(user_file):  # ファイルの存在を確認
        file_status = "exists"
    else:
        file_status = "new"
    if file_status == "exists":  # 既存ユーザーの応答生成
        response = f"こんにちは、{name}さん！前回の情報を基に会話を続けます。"
    else:
        response = f"初めまして、{name}さん！よろしくお願いします。"
    return response  # レスポンスを返す

# テスト用の関数
if __name__ == "__main__":
    test_messages = [
        "川合です。好きな色は赤色です。",
        "吉田です。さっきの話を続けましょう。",
        "さっき話した内容覚えてる？"
    ]

    for msg in test_messages:
        print(f"Input: {msg}")
        print(f"Output: {extract_name(msg)}")
        print()