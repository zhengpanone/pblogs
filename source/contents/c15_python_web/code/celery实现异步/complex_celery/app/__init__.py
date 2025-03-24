from celery import Celery
from flask import Flask

from app.config import BaseConfig

celery = Celery(__name__, broker=BaseConfig.CELERY_BROKER_URL)


def create_app():
    app = Flask(__name__)
    # ....
    celery.conf.update(app.config)  # 更新celery配置

    # ....
    return app
