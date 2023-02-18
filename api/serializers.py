from django.db.models import fields
from rest_framework import serializers
from reserve.models import Reservation
from django.contrib.auth.models import User



class ReservationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reservation
        fields = ['userid', 'doctorid', 'capacity']