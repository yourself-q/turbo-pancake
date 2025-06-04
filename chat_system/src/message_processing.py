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