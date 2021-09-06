from application.celery_tasks.main import app


@app.task(bind=True, retry_backoff=3)
def send_sms(self):
    print("sms_code")
