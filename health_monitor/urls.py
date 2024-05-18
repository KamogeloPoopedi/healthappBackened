from django.contrib import admin
from django.urls import path, include
from prediction.views import PredictRisk

urlpatterns = [
    path('admin/', admin.site.urls),
    path('predict/', PredictRisk.as_view(), name='predict-risk'),
]
