# テスト

このディレクトリには、各モジュールのユニットテストが含まれています。

## 実行方法

1. プロジェクトのルートディレクトリで以下のコマンドを実行して全てのテストを実行します:

```bash
python run_tests.py
```

2. 個々のモジュールのテストを実行する場合は、対応するテストファイルを直接実行します:

```bash
python tests/test_message_processing.py
python tests/test_user_file_management.py
python tests/test_response_generation.py
python tests/test_summary_module.py
```

## テスト内容

- `test_message_processing.py`: メッセージ処理モジュールのテスト
- `test_user_file_management.py`: ユーザーファイル管理モジュールのテスト
- `test_response_generation.py`: レスポンス生成モジュールのテスト
- `test_summary_module.py`: 情報要約モジュールのテスト