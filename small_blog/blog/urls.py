from django.urls import include, path

from . import views

app_name = 'blog'

urlpatterns = [
    path('create/', views.post, name='create'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
    path('<int:pk>/detail/', views.PostDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='edit'),
    path('', views.PostListView.as_view(), name='list'),
]
