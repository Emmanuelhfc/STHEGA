from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseNotFound
from frontend.utils import*
import requests
import logging

logger = logging.getLogger('frontend')
def pareto_front(request, calculation_id):
    endpoint = api_endpoint(request, reverse('API:results_list'))
    endpoint_charts = api_endpoint(request, reverse('API:chart_list'))
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

    files = []
    resp_charts = requests.get(endpoint_charts, params={'calculation_id': calculation_id})
    if resp_charts.status_code == 200:
        charts = resp_charts.json()
        if len(charts) > 0:
            files.extend(charts[0]['files'])

    context = {
        "solutions": results,
        "files": files
    }

    return render(request, 'pareto_front.html', context=context)
