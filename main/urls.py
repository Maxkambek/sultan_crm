from django.urls import path
from . import views

urlpatterns = [
    path('branch-create/', views.BranchCreateAPIView.as_view()),
    path('branch-list/', views.BranchListAPIView.as_view()),
    path('branch/<int:pk>/', views.BranchRetrieveAPIView.as_view()),
    path('paket-create/', views.TourPaketCreateAPIView.as_view()),
    path('paket-list/', views.TourPaketListAPIView.as_view()),
    path('paket-update/<int:pk>/', views.TourPaketUpdateAPIView.as_view()),
    path('client-create/', views.ClientCreateAPIView.as_view()),
    path('client-list/', views.ClientListAPIView.as_view()),
    path('client-full/', views.FullClientListAPIView.as_view()),
    path('client-update/<int:pk>/', views.ClientUpdateAPIView.as_view()),
    path('client-delete/<int:pk>/', views.ClientDeleteAPIView.as_view()),
    path('meeting-create/', views.MeetingCreateAPIView.as_view()),
    path('meeting-update/<int:pk>/', views.MeetingUpdateAPIView.as_view()),
    path('meeting-list/', views.MeetingListAPIView.as_view()),
]
