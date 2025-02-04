from django.shortcuts import render
from django.shortcuts import render, redirect
from frontend.forms import*
from django.urls import reverse
from django.http import HttpResponseBadRequest
from frontend.utils import*
import requests
import logging

logger = logging.getLogger('frontend')


def ga_inputs(request):
    sthe_form_ga = STHEGAForm(request.POST or None)
    filter_input_form = FilterInputGAForm(request.POST or None)
    endpoint_ga = api_endpoint(request, reverse('API:ga_sthe_optimization'))
    endpoint_inputs = api_endpoint(request, reverse('API:inputs_shell_and_tube_list'))

    if filter_input_form.is_valid():
        data = filter_input_form.cleaned_data
        resp_ga = requests.post(endpoint_ga, data=data)
        
        if resp_ga.status_code != 200:
            return HttpResponseBadRequest()
        
        result_id = resp_ga.json()['id']

        return redirect(reverse('frontend:results', kwargs={"pk": result_id}))

    if sthe_form_ga.is_valid():
        
        data = sthe_form_ga.cleaned_data
        data_ga = {}

        data_ga['pop_size'] = data.pop('pop_size')
        data_ga['n_max_gen'] = data.pop('n_max_gen')
        data_ga['fator_area_proj'] = data.pop('fator_area_proj')

        resp_inputs = requests.post(endpoint_inputs, data=data)

        if resp_inputs.status_code != 201:
            return HttpResponseBadRequest()
        
        data_ga['inputs_shell_and_tube'] = resp_inputs.json()['id']

        resp_ga = requests.post(endpoint_ga, data=data_ga)
        
        if resp_ga.status_code != 200:
            return HttpResponseBadRequest()
        
        result_id = resp_ga.json()['id']

        return redirect(reverse('frontend:results', kwargs={"pk": result_id}))
        
        
    context = {
        'new_calculate_form': sthe_form_ga,
        'filter_input_form': filter_input_form
    }

    return render(request, 'filter_new_ga.html', context=context)

