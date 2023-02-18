from django.test import TestCase
from .models import Reservation, Doctor
from api.serializers import ReservationSerializer
from urllib import response
from django.urls import reverse
# Create your tests here.


class UseridTest(TestCase):
    def setUp(self):
        Reservation.objects.create(userid=2)
    def test_doctor_id_content(self):
        reserve = Reservation.objects.get()
        excepted_object_name = f'{reserve.userid}'
        self.assertEqual(excepted_object_name,str(2))



class UseridTest(TestCase):
    def setUp(self):
        Doctor.objects.create(capacity=2)
    def test_doctor_id_content(self):
        reserve = Doctor.objects.get()
        excepted_object_name = f'{reserve.capacity}'
        self.assertEqual(excepted_object_name,str(2))



class HomePageViewTest(TestCase):
    def setUp(self):
        Reservation.objects.create(userid=2)
    def test_view_url_location(self):
        response=self.client.get('')
        self.assertEqual(response.status_code,200)
#test that the name of urls is valid(ok) or no(false)
    def test_view_url_name(self):
        response=self.client.get(reverse('reserve'))#reverse calls(summons) the url name is mentioned in urls.py file
        self.assertEqual(response.status_code,200)
#test template is works or no
    def test_view_url_list(self):
        response=self.client.get(reverse('reserve'))#because the name of this html file in urls in post_list
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed('reservation/reserve.html')#checking the list.html in templaets as an ok test


class SerializersTest(TestCase):
    def test_view_url_location(self):
        response= self.client.get('')
        self.assertEqual(response.status_code,200)
    
    def test_view_url_list(self):
        response1=self.client.get(reverse('main_api_page'))
        response2=self.client.get(reverse('reserve_api_page'))
        self.assertEqual(response1.status_code,200)
        self.assertEqual(response2.status_code,200)
    
