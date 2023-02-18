from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.schemas.coreapi import serializers
from reserve.models import Reservation, Doctor
from .serializers import ReservationSerializer
from django.db.models import Max




@api_view(['GET'])
def get_routes(request):
    routes = [
        {'GET': "/api/"},
        {'POST': "/api/..."},
    ]

    # return JsonResponse(routes, safe=False)
    return Response(routes)



@api_view(['GET','POST'])
def get_reservers(request):
    if request.method == 'GET':
        reserve = Reservation.objects.all()
        serializer = ReservationSerializer(reserve, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        serializer = ReservationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data
        serializer.save()
        doctor = Doctor.objects.order_by('-capacity').first()

        if doctor.capacity > 0 :
            doctor.capacity = (doctor.capacity)-1
            doctor.save()
            return Response('your reservation has been done successsfully!')

        if doctor.capacity <= 0:
            return Response('capacity has been filled')

        return Response('your reservation is done successfully')

