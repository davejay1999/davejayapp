# views.py
from rest_framework import generics
from .models import Bill
from .serializers import BillSerializer

class BillListCreateView(generics.ListCreateAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class BillRetrieveView(generics.RetrieveAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer