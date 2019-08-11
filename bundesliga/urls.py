from django.urls import path
from .views import current_season, season_2018, season_2017, season_2016, season_2015

urlpatterns  = [
    path('', current_season, name='bundeslig'),
    path('season-2018', season_2018, name='season-2018'),
    path('season-2017', season_2017, name='season-2017'),
    path('season-2016', season_2016, name='season-2016'),
    path('season-2015', season_2015, name='season-2015')
]