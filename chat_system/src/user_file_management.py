"""
ユーザーファイル管理モジュール
ユーザーの情報をファイルに保存・読み込む
"""

import os

USER_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "user_data")

def get_user_file_path(name: str) -> str:
    """
    名前からファイルパスを取得

    Args:
        name (str): ユーザーの名前

    Returns:
        str: ファイルパス
    """
    # ディレクトリが存在しない場合は作成
    if not os.path.exists(USER_DATA_DIR):
        os.makedirs(USER_DATA_DIR)

    return os.path.join(USER_DATA_DIR, f"{name}.txt")

def file_exists(file_path: str) -> bool:
    """
    ファイルが存在するか確認

    Args:
        file_path (str): ファイルパス

    Returns:
        bool: ファイルが存在する場合はTrue、そうでない場合はFalse
    """
    return os.path.exists(file_path)

def create_new_user_file(file_path: str, initial_data: str):
    """
    新規ユーザーファイルを作成

    Args:
        file_path (str): ファイルパス
        initial_data (str): 初期データ
    """
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(initial_data)

def load_user_data(file_path: str) -> str:
    """
    ユーザーデータを読み込む

    Args:
        file_path (str): ファイルパス

    Returns:
        str: ユーザーデータ
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# テスト用の関数
if __name__ == "__main__":
    test_name = "test_user"
    file_path = get_user_file_path(test_name)

    if not file_exists(file_path):
        create_new_user_file(file_path, "初期データです。")
        print(f"新規ユーザーファイルを作成しました: {file_path}")

    user_data = load_user_data(file_path)
    print(f"ユーザーデータ: {user_data}")