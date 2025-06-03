"""
レスポンス生成モジュール
LMSTUDIOを用いて過去情報を参照しながら応答を生成
"""

def generate_response(user_name: str, user_data: str, message: str) -> str:
    """
    レスポンスを生成

    Args:
        user_name (str): ユーザーの名前
        user_data (str): ユーザーデータ
        message (str): ユーザーのメッセージ

    Returns:
        str: 生成されたレスポンス
    """
    # TODO: LMSTUDIOを用いて応答を生成するロジックを実装
    # ここではダミーの実装
    if user_data:
        return f"こんにちは、{user_name}さん！前回の情報を基に会話を続けます。"
    else:
        return f"初めまして、{user_name}さん！よろしくお願いします。"

# テスト用の関数
if __name__ == "__main__":
    test_user_name = "テスト太郎"
    test_user_data = "過去の会話データです。"
    test_message = "こんにちは!"

    response = generate_response(test_user_name, test_user_data, test_message)
    print(f"Input: {test_message}")
    print(f"Output: {response}")

    # 新規ユーザーの場合
    response = generate_response(test_user_name, "", test_message)
    print(f"\n新規ユーザーの場合:")
    print(f"Input: {test_message}")
    print(f"Output: {response}")