from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),
    path('', include('blog.urls')),
]
