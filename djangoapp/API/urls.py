"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from API.views import *


tube_diameter_list = TubeDiameterViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

tube_diameter_detail = TubeDiameterViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

inputs_shell_and_tube_list = InputsShellAndTubeViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

inputs_shell_and_tube_detail = InputsShellAndTubeViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

results_list = ResultsViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

results_detail = ResultsViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

chart_list = ChartViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

chart_detail = ChartViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

app_name = 'API'
urlpatterns = [
    # Shell And Tube Inputs
    path('STHECalculation/<int:pk>/', STHECalcultionViewSet.as_view({'post':'shell_and_tube_avaliation'}), name='shell_and_tube_avaliation'),


    path('inputs/', inputs_shell_and_tube_list, name='inputs_shell_and_tube_list'),
    path('inputs/<int:pk>/', inputs_shell_and_tube_detail, name='inputs_shell_and_tube_detail'),

    # Tube Diameter
    path('tube_diameter/', tube_diameter_list, name='tube_diameter_list'),
    path('tube_diameter/<int:pk>/', tube_diameter_detail, name='tube_diameter_detail'),

    # Unit Conversion
    path('unit_conversion/', UnitConversionViewSet.as_view({'post':'conversion'}), name='conversion'),

    # Optmization
    path('sthe/optmization/GA/', STHEOptmizationViewSet.as_view({'post':'ga_sthe_optimization'}), name='ga_sthe_optimization'),
    path('sthe/optmization/NSGA2/', STHEOptmizationViewSet.as_view({'post':'nsga2_sthe_optimization'}), name='nsga2_sthe_optimization'),

    # Results
    path('results/', results_list, name='results_list'),
    path('results/<int:pk>/', results_detail, name='results_detail'),

    # Chart
    path('charts/', chart_list, name='chart_list'),
    path('charts/<int:pk>/', chart_detail, name='chart_detail'),
]
