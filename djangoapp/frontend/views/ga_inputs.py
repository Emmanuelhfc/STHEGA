from django.shortcuts import render
from django.shortcuts import render, redirect
from frontend.forms import*
from django.urls import reverse
from django.http import HttpResponseBadRequest
from frontend.utils import*
import requests
import logging


def ga_inputs(request):
    sthe_form = STHEForm(request.POST or None)
    filter_input_form = FilterInputGAForm(request.POST or None)
    endpoint_ga = api_endpoint(request, reverse('API:ga_sthe_optimization'))

    if filter_input_form.is_valid():
        data = filter_input_form.cleaned_data
        resp_ga = requests.post(endpoint_ga, data=data)
        
        if resp_ga.status_code != 200:
            return HttpResponseBadRequest()
        
        result_id = resp_ga.json()['id']

        return redirect(reverse('frontend:results', kwargs={"pk": result_id}))




    context = {
        'new_calculate_form': sthe_form,
        'filter_input_form': filter_input_form
    }

    return render(request, 'filter_new_ga.html', context=context)

