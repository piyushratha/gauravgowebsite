from django.urls import path
from . import views

app_name = 'queries'

urlpatterns = [
    path('', views.queries_list_all, name='all'),
    path('unread/', views.queries_unread, name='unread'),
    path('read/', views.queries_read, name='read'),
    path('<int:pk>/', views.query_detail, name='detail'),
    path('<int:pk>/toggle/', views.toggle_resolved, name='toggle_resolved'),
    path('<int:pk>/reply/', views.reply_to_query, name='reply'),
    path('<int:pk>/delete/', views.delete_query, name='delete'),
]
