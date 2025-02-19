from django.shortcuts import render, redirect
from frontend.forms import*
from django.urls import reverse
from API.models import TubeCount, TubeInternDiameter
from django.http import HttpResponseServerError
from frontend.utils import*
import requests
import logging

logger = logging.getLogger('frontend')


def avaliation_by_id(request, id):
    path_avaliation = reverse('API:shell_and_tube_avaliation', kwargs={'pk': id})
    endpoint_avaliation = api_endpoint(request, path_avaliation)

    resp_filter = requests.post(endpoint_avaliation)

    if resp_filter.status_code != 200:
        return HttpResponseServerError()

    result_id = resp_filter.json()['id']

    return redirect(reverse('frontend:results', kwargs={'pk': result_id}))
    

def avaliation_inputs(request):
    sthe_form = STHEForm(request.POST or None)
    filter_input_form = FilterInputForm(request.POST or None)
    
    if filter_input_form.is_valid():
        id = filter_input_form.cleaned_data.get('id')
        return avaliation_by_id(request, id)
    
    if sthe_form.is_valid():
        data = sthe_form.cleaned_data

        de = data['pitch'].de   

        data['pitch'] = data['pitch'].id
        
        data['tube_material'] = data['tube_material'].id
        
        bwg = data.pop('bwg')
        di = TubeInternDiameter.objects.get(
            tube_diameter=de,
            standard= bwg
        ).id
        
        data['di'] = di

        
        endpoint_inputs = api_endpoint(request, reverse('API:inputs_shell_and_tube_list'))
        resp_input = requests.post(endpoint_inputs, data=data)
        
        if resp_input.status_code != 201:
            return HttpResponseServerError()
        
        input_id = resp_input.json()['id']
        return avaliation_by_id(request, input_id)

    context = {
        'form_title': "Avaliação",
        'new_calculate_form': sthe_form,
        'filter_input_form': filter_input_form
    }

    return render(request, 'filter_new_avaliation.html', context=context)
