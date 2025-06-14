from django.urls import path
from views import FirstView,SecondView,ThirdView

urlpatterns = [
    path('', FirstView.as_view(), name='one'),
    path('two/', SecondView.as_view(), name='two'),
    path('three/', FirstView.as_view(), name='three')
]
