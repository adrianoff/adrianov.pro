from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('p/<slug:category>/<slug:url>', views.page, name='page'),
]

handler404 = 'adrianov_pro_webpage.views.page404'
handler500 = 'adrianov_pro_webpage.views.page500'