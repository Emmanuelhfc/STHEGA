from django.shortcuts import render


def avaliation_inputs(request):
    context = {
        'form_title': "Avaliação"
    }

    return render(request, 'partials/generic_form.html', context=context)
