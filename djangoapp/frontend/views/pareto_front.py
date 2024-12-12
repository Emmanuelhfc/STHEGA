from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseNotFound
from frontend.utils import*
import requests
import logging

logger = logging.getLogger('frontend')
def pareto_front(request, calculation_id):
    endpoint = api_endpoint(request, reverse('API:results_list'))
    results = []
    first = True
    while True:
        params = {
            'calculation_id': calculation_id
        }
        resp = requests.get(endpoint, params=params)
        
        if resp.status_code != 200:
            return HttpResponseNotFound('Erro na requisição')
            
        
        data = resp.json()

        if len(data['results']) == 0:
            if first:
                return HttpResponseNotFound('Nenhum resultado econtrado para esse cálculo')
            break
        
        results.extend(data['results'])
        
        if not data['next']:
            break

        endpoint = data['next']

    

    context = {
        "solutions": results
    }

    return render(request, 'pareto_front.html', context=context)
