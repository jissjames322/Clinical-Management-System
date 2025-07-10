from rest_framework import serializers
from rootapp.models import Patient, Membership

class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ['MembershipId', 'MembershipType', 'IsActive']
        read_only_fields = ['MembershipId']

class PatientSerializer(serializers.ModelSerializer):
    MembershipDetails = MembershipSerializer(source='MembershipId', read_only=True)
    
    class Meta:
        model = Patient
        fields = [
            'PatientId', 
            'PatientName', 
            'DateOfBirth', 
            'Gender', 
            'MobileNumber', 
            'Address', 
            'MembershipId',
            'MembershipDetails',
            'IsActive'
        ]
        extra_kwargs = {
            'MembershipId': {'write_only': True}
        }

class PatientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            'PatientName', 
            'DateOfBirth', 
            'Gender', 
            'MobileNumber', 
            'Address', 
            'MembershipId'
        ]

class PatientUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            'PatientName', 
            'DateOfBirth', 
            'Gender', 
            'MobileNumber', 
            'Address', 
            'MembershipId',
            'IsActive'
        ]