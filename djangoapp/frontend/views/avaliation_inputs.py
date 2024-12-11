from django.shortcuts import render
from frontend.forms import*


def avaliation_inputs(request):
    sthe_form = STHEForm(request.POST or None)
    filter_input_form = FilterInputForm(request.POST or None)

    context = {
        'form_title': "Avaliação",
        'new_calculate_form': sthe_form,
        'filter_input_form': filter_input_form
    }

    return render(request, 'filter_new.html', context=context)
