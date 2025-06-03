"""
レスポンス生成モジュールのテスト
"""

import unittest
from src.response_generation import generate_response

class TestResponseGeneration(unittest.TestCase):
    def test_generate_response(self):
        # 既存ユーザーの場合
        response = generate_response("佐藤", "過去の会話データです。", "こんにちは!")
        self.assertIn("前回の情報を基に会話を続けます", response)

        # 新規ユーザーの場合
        response = generate_response("鈴木", "", "初めまして")
        self.assertIn("初めまして、鈴木さん！よろしくお願いします", response)

if __name__ == "__main__":
    unittest.main()