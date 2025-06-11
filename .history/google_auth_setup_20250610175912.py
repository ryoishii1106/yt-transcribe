from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle
import os

# Google Docs の書き込み権限を含むスコープ
SCOPES = ['https://www.googleapis.com/auth/documents']

def main():
    creds = None
    # 初回だけトークンを作成
    if not os.path.exists('token.pickle'):
        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secret.json', SCOPES)
        creds = flow.run_local_server(port=0)

        # 認証情報を保存
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
        print("✅ 認証成功。token.pickle を保存しました。")
    else:
        print("token.pickle はすでに存在しています。")

if __name__ == '__main__':
    main()
