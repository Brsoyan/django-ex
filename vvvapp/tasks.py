from .models import AddUser
from datetime import timedelta
from logger_util import ColoredLogger, Fore
from celery import shared_task
from django.utils import timezone # type: ignore

logger = ColoredLogger(__name__)

@shared_task
def run_every_5_minutes_task():
    try:
        threshold_time = timezone.now() - timezone.timedelta(minutes=5)
        users_to_update = AddUser.objects.filter(active=True, modified_at__lte=threshold_time)
    
        updated_count = 0
        for user in users_to_update:
            user.active = False
            user.save(update_fields=['active'])
            updated_count += 1

        logger.info(f'run_every_5_minutes_task executed successfully. Updated {updated_count} records.', color=Fore.GREEN)
    except Exception as e:
        logger.error(f'Error in run_every_5_minutes_task: {str(e)}', color=Fore.RED)

@shared_task
def run_once_a_day_task():
    try:
        threshold_time = timezone.now() - timedelta(days=1)
        deleted_count, _ = AddUser.objects.filter(created_at__lt=threshold_time).delete()
        logger.info(f'run_once_a_day_task executed successfully. Deleted {deleted_count} records.')
    except Exception as e:
        logger.error(f'Error in run_once_a_day_task: {str(e)}')


