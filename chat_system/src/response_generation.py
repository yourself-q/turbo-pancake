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
    # LMSTUDIOを用いて応答を生成するロジックを実装
        # LMSTUDIOのAPIを呼び出して応答を生成する
        # ここでAPIリクエストを作成し、応答を取得する
    # 例: requests.post()を使用してAPIにリクエストを送信する
        # LMSTUDIOのAPIを呼び出して応答を生成する
        if user_data:
        return f"こんにちは、{user_name}さん！前回の情報を基に会話を続けます。"
def call_lmstudio_api(user_name: str, user_data: str, message: str) -> str:
    import requests
    import json
    """
    LMSTUDIOのAPIを呼び出して応答を生成
    
    Args:
    # APIエンドポイントとリクエストデータを設定
    endpoint = "https://api.lmstudio.com/generate"
    payload = {
        "user_name": user_name,
        "user_data": user_data,
        "message": message
    }
    headers = {
        "Content-Type": "application/json"
    }
    # APIリクエストを送信し、応答を取得
    response = requests.post(endpoint, data=json.dumps(payload), headers=headers)
    if response.status_code == 200:
        return response.json().get("response")
    else:
        return "エラーが発生しました。"
        user_name (str): ユーザーの名前
        user_data (str): ユーザーデータ
        message (str): ユーザーのメッセージ
    
    Returns:
        str: 生成されたレスポンス
    """
    # ここでLMSTUDIOのAPIを呼び出すロジックを実装
    # 例: APIリクエストを作成し、応答を取得する
    response = f"これは{user_name}さんへの応答です。"
    return response
        return f"こんにちは、{user_name}さん！前回の情報を基に会話を続けます。"
    else:
        return f"初めまして、{user_name}さん！よろしくお願いします。"
        # LMSTUDIOのAPIを呼び出して応答を生成する
        response = call_lmstudio_api(user_name, user_data, message)
        return response

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