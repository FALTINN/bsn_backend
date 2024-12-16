from django.urls import path

from BSN_app.views import MainView, CatalogView, StoreView

app_name = 'BSN_app'
urlpatterns = [
    path('', MainView.as_view(), name="mainpage"),
    path('catalog', CatalogView.as_view(), name="catalog-page"),
    path('store', StoreView.as_view(), name="store-page"),
]