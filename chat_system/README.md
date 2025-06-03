# LMSTUDIOを用いたユーザー情報記録・管理システム

このプロジェクトは、LMSTUDIOの `devstral-small-2505` モデルを使用してユーザーとの会話を記録・管理するチャットシステムです。

## ディレクトリ構成
```
chat_system/
├── src/              # ソースコード
│   ├── __init__.py
│   ├── message_processing.py  # メッセージ処理モジュール
│   ├── user_file_management.py  # ユーザーファイル管理モジュール
│   ├── response_generation.py  # レスポンス生成モジュール
│   └── summary_module.py  # 情報要約モジュール
├── tests/            # テストコード
│   ├── __init__.py
│   ├── test_message_processing.py
│   ├── test_user_file_management.py
│   ├── test_response_generation.py
│   └── test_summary_module.py
├── user_data/        # ユーザーデータ保存ディレクトリ
└── README.md         # プロジェクト概要
```

## 使用方法
1. LMSTUDIOの `devstral-small-2505` モデルをインストール・設定
2. 各モジュールを実装
3. システム統合を行い、エンドツーエンドの処理フローを確立

## テスト方法
1. ユニットテストを実行
2. 統合テストを実行
3. シナリオテストを実行

## メンテナンス
- ログ管理
- エラーハンドリング
- 定期的なシステム更新