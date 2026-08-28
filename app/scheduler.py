from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime,timezone
from app import create_app,db
from app.models import PasswordResetToken

app = create_app()
scheduler = BlockingScheduler()

@scheduler.scheduled_job("interval",seconds=3600)

def cleanup_tokens():
    with app.app_context():
        deleted = PasswordResetToken.cleanup_expired()
        print(f"[APScheduler] 削除されたトークン数: {deleted}")

if __name__ == "__main__":
    scheduler.start()