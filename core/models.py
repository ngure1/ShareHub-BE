from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _


class Innovation(models.Model):
    STATUS_CHOICES = (
        ("DE", "Deleted"),
        ("P", "Published"),
        ("D", "Draft"),
    )
    DASHBOARD_TYPES = (
        ("S", "Superset"),
        ("M", "Metabase"),
        ("P", "Power BI"),
        ("O", "Other"),
    )
    author = models.ForeignKey(
        "accounts.UserProfile",
        on_delete=models.CASCADE,
        related_name="innovations",
    )
    title = models.CharField(_("Title"), max_length=50)
    description = models.TextField(_("Description"))
    dashboard_link = models.URLField(
        _("Dashboard Link"), max_length=200, blank=True, null=True
    )
    dashboard_image = models.ImageField(
        _("Dashboard preview"),
        upload_to="dashboards/",
        height_field=None,
        width_field=None,
        max_length=None,
        blank=True,
        null=True,
    )
    dashboard_definitions = models.FileField(
        _("Dashboard and Dataset files"),
        upload_to="dashboard_definitions/",
        max_length=100,
        blank=True,
        null=True,
    )
    dashboard_id = models.TextField(_("Dashboard Embed ID"), null=True, blank=True)
    created_at = models.DateTimeField(_("Date created"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Date updated"), auto_now=True)
    status = models.CharField(
        _("Status"), max_length=2, default="P", choices=STATUS_CHOICES
    )
    dashboard_type = models.CharField(
        _("Dashboard Type"), max_length=1, default="O", choices=DASHBOARD_TYPES
    )
    comments_number = models.PositiveIntegerField(
        _("Number of comments"), default=0, blank=True
    )
    likes_number = models.IntegerField(
        _("Number of likes"),
        default=0,
        blank=True,
        validators=[
            MinValueValidator(0),
        ],
    )

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return self.title

    def get_is_liked(self, user):
        return Like.objects.filter(user=user, innovation=self).exists()

    def get_is_bookmarked(self, user):
        return Bookmark.objects.filter(user=user, innovation=self).exists()


class Like(models.Model):
    user = models.ForeignKey(
        "accounts.UserProfile", on_delete=models.CASCADE, related_name="likes"
    )
    innovation = models.ForeignKey(
        Innovation, on_delete=models.CASCADE, related_name="likes"
    )
    created_at = models.DateTimeField(_("Date created"), auto_now_add=True)

    def __str__(self) -> str:
        return self.innovation.title

    def __repr__(self) -> str:
        return self.innovation.title


class Bookmark(models.Model):
    user = models.ForeignKey(
        "accounts.UserProfile", on_delete=models.CASCADE, related_name="bookmarks"
    )
    innovation = models.ForeignKey(
        Innovation, on_delete=models.CASCADE, related_name="user_bookmarks"
    )
    created_at = models.DateTimeField(_("Date created"), auto_now_add=True)


class InnovationComment(models.Model):
    author = models.ForeignKey(
        "accounts.UserProfile",
        on_delete=models.CASCADE,
        related_name="innovation_comments",
    )
    innovation = models.ForeignKey(
        "Innovation", on_delete=models.CASCADE, related_name="innovation_comments"
    )
    text = models.TextField(_("Comment"))
    created_at = models.DateTimeField(_("Date created"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Date updated"), auto_now=True)
    is_edited = models.BooleanField(_("Is edited"), default=False)
