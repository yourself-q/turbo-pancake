"""
情報要約モジュール
LMSTUDIOを用いて会話内容を要約し、ファイルに保存
"""

def summarize_conversation(conversation: str) -> str:
    """
    会話内容を要約

    Args:
        conversation (str): 会話内容

    Returns:
        str: 要約された情報
    """
    # TODO: LMSTUDIOを用いて会話内容を要約するロジックを実装
    # ここではダミーの実装
    return f"summary:{conversation[:50]}..."  # 先頭50文字を要約として返す

def save_summary(file_path: str, summary: str):
    """
    要約をファイルに保存

    Args:
        file_path (str): ファイルパス
        summary (str): 要約内容
    """
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(summary + "\n")

# テスト用の関数
if __name__ == "__main__":
    test_conversation = """
ユーザー: こんにちは、私は佐藤です。好きな色は青です。
システム: 初めまして、佐藤さん！よろしくお願いします。
ユーザー: 最近読んだ本について話したいんですが。
システム: もちろんです、どんな本でしたか？
    """

    summary = summarize_conversation(test_conversation)
    print(f"会話内容:\n{test_conversation}")
    print(f"\n要約: {summary}")

    # 要約をファイルに保存
    test_file_path = "/workspace/chat_system/user_data/test_summary.txt"
    save_summary(test_file_path, summary)
    print(f"\n要約をファイルに保存しました: {test_file_path}")