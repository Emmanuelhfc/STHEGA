from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseServerError
from frontend.forms import*
import requests
from frontend.utils import*
import logging


logger = logging.getLogger('frontend')

def sthe_calculate_by_id(id, request):
    endpoint = api_endpoint(request, reverse('API:shell_and_tube_avaliation', kwargs={'pk': id}))
    resp = requests.post(endpoint)
    if resp.status_code == 200:
        return resp.json().get('id')
    
def calculate_avaliation(request):
    sthe_form = STHEForm(request.POST or None)
    filter_input_form = FilterInputForm(request.POST or None)

    if filter_input_form.is_valid():
        id = filter_input_form.cleaned_data.get('id')
        results_id = sthe_calculate_by_id(id, request)

        if not results_id:
            return HttpResponseServerError('Erro no dimensionamento do trocador de calor casco e tubo!')
        return HttpResponseServerError('Erro no dimensionamento do trocador de calor casco e tubo!')

    # context = {
        
    # }

    # return render(request, 'filter_new.html', context=context)
