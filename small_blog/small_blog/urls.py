from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),
    path('feedback/', include('feedback.urls')),
    path('', include('blog.urls')),
]
