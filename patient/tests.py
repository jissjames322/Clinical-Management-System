from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rootapp.models import Patient, Membership

class PatientManagementTests(APITestCase):
    def setUp(self):
        self.membership = Membership.objects.create(
            MembershipType="Premium",
            IsActive=True
        )
        self.patient_data = {
            'PatientName': 'John Doe',
            'DateOfBirth': '1990-01-01',
            'Gender': 'Male',
            'MobileNumber': '1234567890',
            'Address': '123 Main St',
            'MembershipId': self.membership.MembershipId
        }

    def test_create_patient(self):
        url = reverse('patient-register')
        response = self.client.post(url, self.patient_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Patient.objects.count(), 1)
        self.assertEqual(Patient.objects.get().PatientName, 'John Doe')

    def test_get_patient_list(self):
        Patient.objects.create(**self.patient_data)
        url = reverse('patient-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_deactivate_patient(self):
        patient = Patient.objects.create(**self.patient_data)
        url = reverse('patient-deactivate', kwargs={'PatientId': patient.PatientId})
        response = self.client.patch(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Patient.objects.get(PatientId=patient.PatientId).IsActive)