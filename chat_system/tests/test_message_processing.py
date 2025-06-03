"""
メッセージ処理モジュールのテスト
"""

import unittest
from src.message_processing import extract_name

class TestMessageProcessing(unittest.TestCase):
    def test_extract_name(self):
        # 名前が含まれる場合
        self.assertIn("%*name,川合", extract_name("川合です。好きな色は赤色です。"))
        self.assertIn("%*name,吉田", extract_name("吉田です。さっきの話を続けましょう。"))

        # 名前が含まれない場合
        self.assertEqual(extract_name("さっき話した内容覚えてる？"), "%*name,unknown*%")

if __name__ == "__main__":
    unittest.main()