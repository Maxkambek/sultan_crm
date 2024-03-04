from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginAPIView.as_view()),
    path('faq/', views.FAQListAPIView.as_view()),
    path('register/', views.RegisterAPIView.as_view()),
    path('top-operators/', views.TopOperatorListAPIView.as_view()),
    path('user-rud/', views.AccountRUDAPIView.as_view()),
    path('top-stats/', views.CommonStatsAPIView.as_view()),
    path('list-workers/', views.ListOfWorkersAPIView.as_view()),
    path('count-clients/', views.CountOfClientsAPIView.as_view()),
]
