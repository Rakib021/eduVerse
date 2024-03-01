
from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # new


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app_users.urls')),
    path('curriculum/',include('curriculum.urls')),
]
urlpatterns += staticfiles_urlpatterns() # new


from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,
                         document_root = settings.MEDIA_ROOT)