from django.db.models import Q
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser
from .serializers import FormulaSerializer, QuestionSerializer, SymptomQuestionSerializer, SymptomSerializer
from .models import Symptom, SymptomFormula, SymptomQuestion

# Create your views here.
class SymptomViewSet(ModelViewSet):
    queryset = Symptom.objects.all()
    serializer_class = SymptomSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve', 'requestsymptom', 'getresult']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        Symptom.objects.filter(pk=kwargs['pk']).update(view_count=instance.view_count + 1)
        serializer = SymptomQuestionSerializer(instance,  context=self.get_serializer_context())
        return Response(serializer.data)

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

    
    def diagnosis_disease(self, formulas, options):
        results = []
        for formula in formulas:
            s = 0
            for item in formula.options.all():
                index = str(item.option.id)
                if index in options:
                    s += options[index]
            
            if(s > formula.sum):
                results.append(formula.result)

        print(results)
        return results

    @action(detail=False, methods=['POST'], permission_classes=[])
    def getresult(self, request):
        symptom_id = request.data["symptom_id"]
        options = request.data["options"]
        formulas = SymptomFormula.objects.filter(symptom_id=symptom_id).prefetch_related('options').all()

        results = self.diagnosis_disease(formulas, options)

        return Response(results)


class QuestionViewSet(ModelViewSet):
    queryset = SymptomQuestion.objects.all()
    serializer_class = QuestionSerializer

    def get_permissions(self):
        if self.request.method in ['PATCH', 'DELETE', 'PUT', 'POST']:
            return [IsAdminUser()]
        return [AllowAny()]
