from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rootapp.models import Patient, Membership
from .serializers import PatientSerializer, MembershipSerializer


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.filter(IsActive=True)
    serializer_class = PatientSerializer
    
    
    #  Enable search
    filter_backends = [filters.SearchFilter]
    search_fields = ['PatientName', 'PatientId']

    def destroy(self, request, *args, **kwargs):
        # Soft delete
        patient = self.get_object()
        patient.IsActive = False
        patient.save()
        return Response({"message": "Patient deactivated"}, status=status.HTTP_204_NO_CONTENT)

class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.filter(IsActive=True)
    serializer_class = MembershipSerializer

    def destroy(self, request, *args, **kwargs):
        # Soft delete
        membership = self.get_object()
        membership.IsActive = False
        membership.save()
        return Response({"message": "Membership deactivated"}, status=status.HTTP_204_NO_CONTENT)
