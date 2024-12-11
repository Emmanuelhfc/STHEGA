from django.shortcuts import render


def nsga2_inputs(request):
    context = {
        'form_title': "NSGA-II"
    }

    return render(request, 'partials/generic_form.html', context=context)
