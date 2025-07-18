from flask import current_app
from celery.utils.log import get_task_logger

from app import celery

logger = get_task_logger(__name__)

@celery.task
def send_email(to, subject, content):
    app = current_app._get_current_object()
    subject = app.config['EMAIL_SUBJECT_PREFIX'] + subject
    logger.info('send message "%s" to %s', (content, to))
    return do_send_email(to, subject, content)
