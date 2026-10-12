import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
import sys

sys.stdout.reconfigure(encoding='utf-8')

key_path = "D:/VentopiaSystem/ventopia_portal_server_backup/credentials/service_account.json"
SCOPES = ["https://www.googleapis.com/auth/indexing"]

try:
    credentials = service_account.Credentials.from_service_account_file(
        key_path, scopes=SCOPES
    )
    service = build("indexing", "v3", credentials=credentials)
    
    urls = [
        "https://nouvelleworkz.com/commercial/reinstatement/",
        "https://nouvelleworkz.com/commercial/commercial-renovation/office-renovation/",
        "https://nouvelleworkz.com/office-reinstatement-cost-guide-singapore-psf-budgeting/",
        "https://nouvelleworkz.com/jtc-factory-warehouse-reinstatement-singapore-handover-rules/"
    ]
    
    for u in urls:
        body = {
            "url": u,
            "type": "URL_UPDATED"
        }
        res = service.urlNotifications().publish(body=body).execute()
        print(f"Submitted {u}:")
        print(f"  Notify time: {res.get('urlNotificationMetadata', {}).get('latestUpdate', {}).get('notifyTime')}")
        
except Exception as e:
    print(f"Indexing API notice: {e}")
