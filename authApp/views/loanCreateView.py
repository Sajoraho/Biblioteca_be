from rest_framework import status, views 
from rest_framework.response import Response 
from authApp.serializers.loanSerializer import LoanSerializer 

class LoanCreateView(views.APIView): 
 
    def post(self, request, *args, **kwargs): 
        serializer = LoanSerializer(data=request.data) 
        serializer.is_valid(raise_exception=True) 
        serializer.save() 
             
        return Response(serializer.data, status=status.HTTP_201_CREATED) 