from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/documents', 'https://www.googleapis.com/auth/drive']


def write_to_google_doc(text, title="Transcribed Text", folder_id=None):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    docs_service = build('docs', 'v1', credentials=creds)
    drive_service = build('drive', 'v3', credentials=creds)

    # Google Docs を作成
    doc = docs_service.documents().create(body={"title": title}).execute()
    doc_id = doc.get('documentId')

    # テキストを書き込み
    docs_service.documents().batchUpdate(
        documentId=doc_id,
        body={'requests': [{'insertText': {'location': {'index': 1}, 'text': text}}]}
    ).execute()

    # Driveのフォルダに移動（必要なら）
    if folder_id:
        # まず既存のparents（マイドライブ）から外す
        file_metadata = drive_service.files().get(fileId=doc_id, fields='parents').execute()
        previous_parents = ",".join(file_metadata.get('parents', []))

        drive_service.files().update(
            fileId=doc_id,
            addParents=folder_id,
            removeParents=previous_parents,
            fields='id, parents'
        ).execute()

    return f"https://docs.google.com/document/d/{doc_id}"