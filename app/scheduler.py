from apscheduler.schedulers.background import BackgroundScheduler
from app.models import PasswordResetToken

scheduler = None

def cleanup_tokens(app):
    with app.app_context():
        deleted = PasswordResetToken.cleanup_expired()
        print(f"[APScheduler] 削除されたトークン数: {deleted}")

def init_scheduler(app):
    global scheduler

    if scheduler is None:
        scheduler = BackgroundScheduler()
        scheduler.add_job(
            func=lambda:cleanup_tokens(app),
            trigger="interval",
            seconds=3600,
            id="cleanup_tokens_job",
            replace_existing=True
        )
        scheduler.start()

#　※本番環境……3600秒(1時間ごと)、テスト用……10秒ごと。
