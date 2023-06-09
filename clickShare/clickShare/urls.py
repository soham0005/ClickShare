"""clickShare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from home.views import *

urlpatterns = [
        
    #path('', index),
    path('',index, name='index'),
    path('about/',about, name='about'),
    # path('',index,name="index"),
    path('download/<uid>/',download),
    path('handle/',Handle_Uploaded_Files.as_view()),
    path('email/',sendEmail),
    path('error/',error),
    path('contact/',contact,name="contact"),
    path('admin/', admin.site.urls),
    # path('',include("home.urls")),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()