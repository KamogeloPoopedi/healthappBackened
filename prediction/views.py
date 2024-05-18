from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserInput  # Import UserInput model instead of UserInputSerializer
from .serializers import UserInputSerializer
# import numpy as np
# import tensorflow as tf

class PredictRisk(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserInputSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            # Here you would load and use your trained TensorFlow model
            # For this example, let's use a dummy prediction
            age = data['age']
            bmi = data['bmi']
            blood_pressure = data['blood_pressure']

            # Dummy prediction logic (replace with actual model prediction)
            risk_score = (age + bmi + blood_pressure) / 3
            risk = "High" if risk_score > 50 else "Low"

            return Response({'risk': risk, 'risk_score': risk_score}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
