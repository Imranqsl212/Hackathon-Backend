from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("user_auth.urls")),
]

#css and js for gunicorn
urlpatterns += staticfiles_urlpatterns()
