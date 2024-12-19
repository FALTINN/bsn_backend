from django.urls import path

from BSN_app.views import MainView

app_name = 'BSN_app'
urlpatterns = [
    path('', MainView.as_view(), name="mainpage"),
    path('rich', MainView.as_view(), name="rich-page"),
    path('king', MainView.as_view(), name="king-page"),
    path('builder', MainView.as_view(), name="builder-page"),
    path('redstoner', MainView.as_view(), name="redstoner-page"),
    path('creator', MainView.as_view(), name="creator-page"),
    path('building', MainView.as_view(), name="building-page"),
    path('event', MainView.as_view(), name="event-page"),
]