"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

import project01
from project01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('index', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('information', views.information, name='information'),
    path('info', views.info, name='info'),
    path('test', views.test, name='test'),
    path('table', views.table, name='table'),
    path('datatable', views.datatable, name='datatable'),
    path('chart', views.chart, name='chart'),
    path('authregister', views.authregister, name='authregister'),
    path('authforgotpassword', views.authforgotpassword, name='authforgotpassword'),
    path('social', views.social, name='social'),
    path('health', views.health, name='health'),
    path('gdp', views.gdp, name='gdp'),
    path('etc', views.etc, name='etc'),
    path('summary', views.summary, name='summary'),
    path('info2', views.info2, name='info2'),
    path('covid19', views.covid19, name='covid19'),
    path('militarypower', views.militarypower, name='militarypower'),
    path('illiteracyrate', views.illiteracyrate, name='illiteracyrate'),
    path('summary2', views.summary2, name='summary2'),
    path('regi_done', views.regi_done, name='regi_done'),
    path('logout/', views.logout, name='logout'),
    # path('highchart', views.highchart, name='highchart'),
]
