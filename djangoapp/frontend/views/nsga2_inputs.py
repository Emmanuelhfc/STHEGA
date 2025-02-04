from django.shortcuts import render, redirect
from frontend.forms import*
from django.urls import reverse
from django.http import HttpResponseBadRequest
from frontend.utils import*
import requests
import logging

logger = logging.getLogger('frontend')

def nsga2_inputs(request):
    sthe_nsga_form = STHENSGAForm(request.POST or None)
    filter_input_form = FilterInputNSGA2Form(request.POST or None)
    endpoint_nsga2 = api_endpoint(request, reverse('API:nsga2_sthe_optimization'))
    endpoint_inputs = api_endpoint(request, reverse('API:inputs_shell_and_tube_list'))

    if filter_input_form.is_valid():
        data = filter_input_form.cleaned_data
        resp_nsga2 = requests.post(endpoint_nsga2, data=data)
        
        if resp_nsga2.status_code != 200:
            return HttpResponseBadRequest()
        
        calculation_id = resp_nsga2.json()[0]['calculation_id']

        return redirect(reverse('frontend:pareto_front', kwargs={"calculation_id": calculation_id}))
    
    if sthe_nsga_form.is_valid():
        data = sthe_nsga_form.cleaned_data
        data_nsga = {}

        data_nsga['pop_size'] = data.pop('pop_size')
        data_nsga['n_max_gen'] = data.pop('n_max_gen')

        resp_inputs = requests.post(endpoint_inputs, data=data)

        if resp_inputs.status_code != 201:
            return HttpResponseBadRequest()
        
        data_nsga['inputs_shell_and_tube'] = resp_inputs.json()['id']

        resp_nsga2 = requests.post(endpoint_nsga2, data=data_nsga)
        
        if resp_nsga2.status_code != 200:
            return HttpResponseBadRequest()
        
        calculation_id = resp_nsga2.json()[0]['calculation_id']

        return redirect(reverse('frontend:pareto_front', kwargs={"calculation_id": calculation_id}))


    context = {
        'form_title': "Avaliação",
        'new_calculate_form': sthe_nsga_form,
        'filter_input_form': filter_input_form
    }

    return render(request, 'filter_new_nsga2.html', context=context)

