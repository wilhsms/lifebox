from django.contrib.auth import signals, get_user_model
from django.db import transaction

from easyaudit.middleware.easyaudit import get_current_request
from easyaudit.models import LoginEvent
from easyaudit.settings import WATCH_AUTH_EVENTS

def user_logged_in(sender, request, user, **kwargs):
    try:
        with transaction.atomic():
            login_event = LoginEvent.objects.create(login_type=LoginEvent.LOGIN,
                                     username=getattr(user, user.USERNAME_FIELD),
                                     user=user,
                                     remote_ip=request.META['REMOTE_ADDR'])
    except:
        pass


def user_logged_out(sender, request, user, **kwargs):
    try:
        with transaction.atomic():
            login_event = LoginEvent.objects.create(login_type=LoginEvent.LOGOUT,
                                                    username=getattr(user, user.USERNAME_FIELD),
                                                    user=user,
                                                    remote_ip=request.META['REMOTE_ADDR'])
    except:
        pass


def user_login_failed(sender, credentials, **kwargs):
    try:
        with transaction.atomic():
            request = get_current_request() # request argument not available in django < 1.11
            user_model = get_user_model()
            login_event = LoginEvent.objects.create(login_type=LoginEvent.FAILED,
                                                    username=credentials[user_model.USERNAME_FIELD],
                                                    remote_ip=request.META['REMOTE_ADDR'])
    except:
        pass


if WATCH_AUTH_EVENTS:
    signals.user_logged_in.connect(user_logged_in, dispatch_uid='easy_audit_signals_logged_in')
    signals.user_logged_out.connect(user_logged_out, dispatch_uid='easy_audit_signals_logged_out')
    signals.user_login_failed.connect(user_login_failed, dispatch_uid='easy_audit_signals_login_failed')