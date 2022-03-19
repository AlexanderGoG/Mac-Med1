from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from core.models import Obrashenie, PolEnum, Status, Problems
from core.serializers import ObrashenieSerializer

# API - модели
class ObrashenieViewSet(ModelViewSet):
    queryset = Obrashenie.objects.all()
    serializer_class = ObrashenieSerializer
    http_method_names = ['post',]

class ObrashenieList(APIView):
    def get(self, request, format=None):
        snippets = Obrashenie.objects.all()
        serializer = ObrashenieSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ObrashenieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def render_home(request):
    list_obrashenii = []

    obrashenie=Obrashenie.objects.all()

    return render(
        request,
        'core/home.html', {'obrashenie': obrashenie})
def render_form(request):
    return render(
        request,
        'core/form_add.html',
        {
            'pol_list':PolEnum,
            'status_list':Status.objects.all(),
            'problem_list':Problems.objects.all(),
        }
    )