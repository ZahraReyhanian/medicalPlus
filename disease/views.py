from django.db.models import Q
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .serializers import SymptomSerializer
from .models import Symptom

# Create your views here.
class SymptomViewSet(ModelViewSet):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer

    def set_gender_adult(self, request):
        gender = request.data["gender"]
        age = int(request.data["age"])
        adult = True
        if age < 18:
            adult = False

        if gender == "female":
            gender = "F"
        if gender == "male":
            gender = "M"

        return adult, adult

    #todo update viewCount

    @action(detail=False, methods=['POST'], permission_classes=[])
    def requestsymptom(self, request):
        gender, adult = self.set_gender_adult(request)

        symptoms = Symptom.objects.filter(adult=adult).filter(Q(gender="B") | Q(gender=gender))
        
        serializer = SymptomSerializer(symptoms, many=True)
        return Response(serializer.data)