from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

# Google Docs APIのスコープ
SCOPES = ['https://www.googleapis.com/auth/documents']

def write_to_google_doc(text, title="Transcribed Text"):
    # 認証済みの token.json を使う
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # Google Docs APIに接続
    service = build('docs', 'v1', credentials=creds)

    # 新しいドキュメントを作成
    document = service.documents().create(body={"title": title}).execute()
    doc_id = document['documentId']

    # テキストを書き込む
    requests = [
        {
            'insertText': {
                'location': {
                    'index': 1
                },
                'text': text
            }
        }
    ]
    service.documents().batchUpdate(
        documentId=doc_id,
        body={'requests': requests}
    ).execute()

    print("✅ 成功！Google Docs のURLはこちら:")
    print(f"https://docs.google.com/document/d/{doc_id}")


# テスト実行
if __name__ == "__main__":
    sample_text = "こんにちは、これは ChatGPT と Ryo の連携テストです！"
    write_to_google_doc(sample_text)