from authApp.models.loan import Loan
from rest_framework import serializers
class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ['id', 'date_borrow', 'date_agreed', 'date_return', 'book', 'register']