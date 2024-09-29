"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # admin page's urls
    path("admin/", admin.site.urls),
    # login, logout, password changing, password resetting
    path('accounts/', include("allauth.urls")),
    path('books/', include("books.urls")),
    path("", include('pages.urls')),

] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)


# just use debug_toolbar on development environment:
if settings.DEBUG:
    from debug_toolbar.toolbar import debug_toolbar_urls
    urlpatterns = [
        *urlpatterns,
    ] + debug_toolbar_urls()
