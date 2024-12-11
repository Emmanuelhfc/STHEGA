from django.shortcuts import render


def results(request, pk):
    context = {
        
    }

    return render(request, 'results.html', context=context)
