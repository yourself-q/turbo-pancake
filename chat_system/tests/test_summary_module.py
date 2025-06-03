"""
情報要約モジュールのテスト
"""

import unittest
import os
from src.summary_module import summarize_conversation, save_summary

class TestSummaryModule(unittest.TestCase):
    def setUp(self):
        self.test_file_path = "/workspace/chat_system/user_data/test_summary.txt"
        # テスト用ファイルが存在する場合は削除
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_summarize_conversation(self):
        conversation = """
ユーザー: こんにちは、私は佐藤です。好きな色は青です。
システム: 初めまして、佐藤さん！よろしくお願いします。
ユーザー: 最近読んだ本について話したいんですが。
システム: もちろんです、どんな本でしたか？
        """
        summary = summarize_conversation(conversation)
        self.assertTrue(summary.startswith("summary:"))
        self.assertIn("ユーザー: こんにちは", summary)

    def test_save_summary(self):
        summary = "summary:テストの要約です。"
        save_summary(self.test_file_path, summary)

        # ファイルが存在することを確認
        self.assertTrue(os.path.exists(self.test_file_path))

        # ファイル内容を読み込む
        with open(self.test_file_path, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn(summary, content)

    def tearDown(self):
        # テスト用ファイルを削除
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

if __name__ == "__main__":
    unittest.main()