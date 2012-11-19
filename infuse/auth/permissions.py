from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.exceptions import PermissionDenied, ImproperlyConfigured

__author__ = "Derek Stegelman"

class LoginRequiredMixin(object):
    """
    View mixin for requiring a Login.
    """

    login_url = settings.LOGIN_URL

    @method_decorator(login_required(login_url=login_url))
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class SuperUserRequiredMixin(object):
    """
    Require a logged in Superuser
    """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied

        return super(SuperUserRequiredMixin, self).dispatch(request, *args, **kwargs)

class StaffRequiredMixin(object):
    """
    Require Staff
    """

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied

        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


class GroupRequiredMixin(object):
    """
    View mixin which verifies that the logged in user has the specified
    Group.

    Make sure to use the LoginRequiredMixin ahead of this.

    Raises a 403 Permission Denied Error.

    """
    group = None

    def dispatch(self, request, *args, **kwargs):
        if not self.group:
            raise ImproperlyConfigured("No group provided.")

        if not bool(request.user.groups.filter(name=self.group)):
            raise PermissionDenied

        return super(GroupRequiredMixin, self).dispatch(request,
            *args, **kwargs)