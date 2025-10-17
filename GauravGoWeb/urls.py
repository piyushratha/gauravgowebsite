"""GauravGoWeb URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from gauravgowebsite import views
from gauravgowebsite.views import *
from django.conf import settings
from django.conf.urls.static import static


app_name = 'queries'   # <-- required for namespacing


urlpatterns = [
    path('admin/queries/', include('gauravgowebsite.urls', namespace='queries')),
    path('admin/', admin.site.urls),
    path('djadmin/', admin.site.urls),
    path('admin_home/', views.admin_home, name="admin_home"),
    path('', index, name="index"),
    path('games', games, name="games"),
    path('services', services, name="services"),
    path('about', about, name="about"),
    path('advertisers', advertisers, name="advertisers"),
    path('careers', careers, name="careers"),
    path('media_coverage', media_coverage, name="media_coverage"),
    path('our_supporters', our_supporters, name="our_supporters"),
    path('privacy_policy', privacy_policy, name="privacy_policy"),
    path('header', header, name="header"),
    path('footer', footer, name="footer"),
    path('simulation-projects', simulation_projects, name="simulation_projects"),
    path('3d-assets', three_d_assets, name="three_d_assets"),
    path('game-development', game_development, name="game_development"),
    path('animation', animation, name="animation"),
    path('blender-vfx', blender_vfx, name="blender_vfx"),
    path('admin_login', admin_login, name="admin_login"),
    path('admin_home', admin_home, name="admin_home"),
    path('logout', Logout, name="logout"),
    path('search', search, name="search"),
    path('change_password', change_password, name="change_password"),
    path('add_games', add_games, name="add_games"),
    # path('add_views_games', add_views_games, name="add_views_games"),
    path('manage_games', manage_games, name="manage_games"),
    path('edit_game/<int:pid>', edit_games, name="edit_game"),
    path('delete_game/<int:pid>', delete_games, name="delete_game"),
    # Public contact form submission endpoint
    path('submit-query/', views.submit_query, name='submit_query'),
    path('', views.queries_list_all, name='all'),
    path('unread/', views.queries_unread, name='unread'),
    path('read/', views.queries_read, name='read'),
    path('<int:pk>/', views.query_detail, name='detail'),
    path('<int:pk>/toggle/', views.toggle_resolved, name='toggle_resolved'),
    path('<int:pk>/reply/', views.reply_to_query, name='reply'),
    path('<int:pk>/delete/', views.delete_query, name='delete'),

        # ... other paths ...

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
