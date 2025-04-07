"""
URL configuration for final_project_python project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from myapp.views import  home_view , product_view,details_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path("",home_view,name="home"),
    path("products/",product_view,name="products"),
    path("details/<int:pk>/", details_view),
    path("_reload_/",include("django_browser_reload.urls")),
    path("", include("users.url")),
    
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


