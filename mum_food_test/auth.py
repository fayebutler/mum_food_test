from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class IsAuthenticatedOrReadLikeOnly(BasePermission):
    """
    Based off IsAuthenticatedOrReadOnly
    The request is authenticated as a user,
                or is a read-only request
                or is a post to like action.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            view.action == "like" or
            request.user and
            request.user.is_authenticated
        )


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
