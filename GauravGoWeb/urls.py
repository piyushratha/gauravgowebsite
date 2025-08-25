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
from gauravgowebsite.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
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
    
        
]
