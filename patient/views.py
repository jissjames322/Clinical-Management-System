from rest_framework import generics, status, filters
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rootapp.models import Patient, Membership
from .serializers import (
    PatientSerializer,
    PatientCreateSerializer,
    PatientUpdateSerializer,
    MembershipSerializer
)

class PatientRegistrationView(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientCreateSerializer

class PatientListView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['PatientName', 'MobileNumber', 'MembershipId__MembershipType']

class PatientDetailView(generics.RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_field = 'PatientId'

class PatientUpdateView(generics.UpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientUpdateSerializer
    lookup_field = 'PatientId'

class PatientDeactivateView(generics.UpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_field = 'PatientId'

    def perform_update(self, serializer):
        serializer.save(IsActive=False)

class MembershipListView(generics.ListAPIView):
    queryset = Membership.objects.filter(IsActive=True)
    serializer_class = MembershipSerializer