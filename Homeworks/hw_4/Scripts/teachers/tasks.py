from celery import shared_task

from django.core.mail import send_mail


@shared_task
def del_logs():
    import datetime

    from teachers.models import Logger
    from django.utils.timezone import now

    start_date = now()
    end_date = start_date - datetime.timedelta(days=7)
    Logger.objects.filter(created__lte=end_date).delete()


@shared_task
def send_lmail(request, *args, **kwargs):
    send_mail(request.get('title'),
              request.get('message'),
              'hilleldjango123456@gmail.com',
              [request.get('email_from')])
