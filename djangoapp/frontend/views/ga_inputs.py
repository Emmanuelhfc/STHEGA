from django.shortcuts import render


def ga_inputs(request):
    context = {
        'form_title': "GA"
    }

    return render(request, 'partials/generic_form.html', context=context)
