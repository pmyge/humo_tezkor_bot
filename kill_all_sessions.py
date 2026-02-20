import requests
import sys

TOKEN = "8354261773:AAFcVFIYIHRZ-9koTGSXaAtDo6zr-e-H3HI"

def kill_sessions():
    print(f"--- Terminating sessions for Bot ID: {TOKEN.split(':')[0]} ---")
    
    # 1. Close (for polling)
    try:
        r = requests.post(f"https://api.telegram.org/bot{TOKEN}/close")
        print(f"Close result: {r.json()}")
    except Exception as e:
        print(f"Close failed: {e}")

    # 2. LogOut (Aggressive)
    try:
        r = requests.post(f"https://api.telegram.org/bot{TOKEN}/logOut")
        print(f"LogOut result: {r.json()}")
    except Exception as e:
        print(f"LogOut failed: {e}")

    # 3. Delete Webhook
    try:
        r = requests.post(f"https://api.telegram.org/bot{TOKEN}/deleteWebhook", params={"drop_pending_updates": True})
        print(f"Delete Webhook result: {r.json()}")
    except Exception as e:
        print(f"Delete Webhook failed: {e}")

    # 4. Drain updates (just in case polling is stuck)
    try:
        r = requests.get(f"https://api.telegram.org/bot{TOKEN}/getUpdates", params={"offset": -1})
        print(f"Drain updates result: {r.json()}")
    except Exception as e:
        print(f"Drain failed: {e}")

if __name__ == "__main__":
    kill_sessions()
