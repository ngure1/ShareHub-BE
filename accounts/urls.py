from django.urls import path, include
from . import views
from . import signals


urlpatterns = [
    path("auth/", include("djoser.urls")),
    path(
        "auth/jwt/create/",
        view=views.CustomTokenObtainPairView.as_view(),
        name="token-obtain_pair",
    ),
    path(
        "auth/jwt/refresh/",
        view=views.CustomTokenRefreshView.as_view(),
        name="token-refresh",
    ),
    path(
        "auth/jwt/verify/",
        view=views.CustomTokenVerifyView.as_view(),
        name="token-verify",
    ),
    path("auth/logout/", view=views.LogoutView.as_view(), name="auth-logout"),
    path("profiles/", views.user_profile_list, name="userprofile-list"),
    path("profiles/<int:pk>/", views.user_profile_detail, name="userprofile-detail"),
    path(
        "profiles/<int:pk>/innovations/",
        views.user_innovation_list,
        name="userinnovation-list",
    ),
    path("profiles/me/", views.me_user_profile, name="userprofile-detail"),
]
