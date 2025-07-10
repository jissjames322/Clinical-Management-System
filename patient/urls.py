from django.urls import path
from . import views

urlpatterns = [
    # Patient endpoints
    path('register/', views.PatientRegistrationView.as_view(), name='patient-register'),
    path('list/', views.PatientListView.as_view(), name='patient-list'),
    path('<int:PatientId>/', views.PatientDetailView.as_view(), name='patient-detail'),
    path('<int:PatientId>/update/', views.PatientUpdateView.as_view(), name='patient-update'),
    path('<int:PatientId>/deactivate/', views.PatientDeactivateView.as_view(), name='patient-deactivate'),
    
    # Membership endpoints
    path('memberships/', views.MembershipListView.as_view(), name='membership-list'),
]