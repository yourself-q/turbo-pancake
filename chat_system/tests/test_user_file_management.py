"""
ユーザーファイル管理モジュールのテスト
"""

import unittest
import os
from src.user_file_management import (
    get_user_file_path,
    file_exists,
    create_new_user_file,
    load_user_data
)

class TestUserFileManagement(unittest.TestCase):
    def setUp(self):
        self.test_name = "test_user"
        self.file_path = get_user_file_path(self.test_name)
        # テスト用ファイルが存在する場合は削除
        if file_exists(self.file_path):
            os.remove(self.file_path)

    def test_create_and_load_user_file(self):
        # 新規ユーザーファイルを作成
        create_new_user_file(self.file_path, "初期データです。")

        # ファイルが存在することを確認
        self.assertTrue(file_exists(self.file_path))

        # データを読み込む
        user_data = load_user_data(self.file_path)
        self.assertEqual(user_data, "初期データです。")

    def tearDown(self):
        # テスト用ファイルを削除
        if file_exists(self.file_path):
            os.remove(self.file_path)

if __name__ == "__main__":
    unittest.main()