"""
全てのテストを実行するスクリプト
"""

import unittest

def run_all_tests():
    # テストディレクトリを指定して全てのテストを実行
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover("tests", pattern="test_*.py")

    # テストランナーを作成し、テストスイートを実行
    test_runner = unittest.TextTestRunner(verbosity=2)
    results = test_runner.run(test_suite)

    # テスト結果を返す
    return results

if __name__ == "__main__":
    results = run_all_tests()
    print(f"テスト実行結果: {results}")