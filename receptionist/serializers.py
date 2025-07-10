from rest_framework import serializers
from rootapp.models import Patient, Membership

# serializers.py
class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ['MembershipId', 'MembershipType']

class PatientSerializer(serializers.ModelSerializer):
    # Accept only the ID, not the nested object
    MembershipId = serializers.PrimaryKeyRelatedField(
        queryset=Membership.objects.all()
    )

    class Meta:
        model = Patient
        fields = '__all__'