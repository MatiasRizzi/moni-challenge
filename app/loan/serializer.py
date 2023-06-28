from rest_framework import serializers

from loan.models import Loan
from validator_id import validate_dni

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'

    def validate(self, data):
        number_dni = data.get("number_dni", None)

        if not validate_dni(number_dni):
            raise serializers.ValidationError("This number is not authorised for credit")

        return data 
