from django.conf import settings 
from rest_framework import generics, status 
from rest_framework.response import Response 
from rest_framework_simplejwt.backends import TokenBackend 
from rest_framework.permissions import IsAuthenticated 
 
from authApp.models.loan import Loan 
from authApp.serializers.loanSerializer import LoanSerializer 

class UserDetailView(generics.RetrieveAPIView): 
    queryset = Loan.objects.all() 
    serializer_class = LoanSerializer 