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
    param_poiska = {}
    obrashenie=Obrashenie.objects.all()
    if request.GET.get('first_name'):
        param_poiska['first_name']=request.GET.get('first_name')
        obrashenie=obrashenie.filter(first_name__icontains=request.GET.get('first_name'))
    if request.GET.get('second_name'):
        param_poiska['second_name'] = request.GET.get('second_name')
        obrashenie=obrashenie.filter(second_name__icontains=request.GET.get('second_name'))
    if request.GET.get('otchestvo'):
        param_poiska['otchestvo'] = request.GET.get('otchestvo')
        obrashenie=obrashenie.filter(otchestvo__icontains=request.GET.get('otchestvo'))
    if request.GET.get('phone'):
        param_poiska['phone'] = request.GET.get('phone')
        obrashenie=obrashenie.filter(phone__icontains=request.GET.get('phone'))
    if request.GET.get('vozrast'):
        param_poiska['vozrast'] = request.GET.get('vozrast')
        obrashenie=obrashenie.filter(vozrast=request.GET.get('vozrast'))
    if request.GET.get('pol'):
        param_poiska['pol'] = int(request.GET.get('pol'))
        obrashenie=obrashenie.filter(pol=request.GET.get('pol'))
    if request.GET.get('adress'):
        param_poiska['adress'] = request.GET.get('adress')
        obrashenie=obrashenie.filter(adress__icontains=request.GET.get('adress'))
    if request.GET.get('problem'):
        param_poiska['problem'] = int(request.GET.get('problem'))
        obrashenie=obrashenie.filter(problems_id=request.GET.get('problem'))
    if request.GET.get('status'):
        param_poiska['status'] = int(request.GET.get('status'))
        obrashenie=obrashenie.filter(status_id=request.GET.get('status'))
    return render(
        request,
        'core/home.html', {'obrashenie': obrashenie,
                           'pol_list': PolEnum,
                           'status_list': Status.objects.all(),
                           'problem_list': Problems.objects.all(),
                          'param_poiska':param_poiska,
                           })
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