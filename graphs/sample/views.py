from chartit import DataPool, Chart
from graphs.sample.models import MonthlyWeatherByCity
from django.shortcuts import render_to_response
from chartit.templatetags.chartit import load_charts

def weather_chart_view(request):
    #Step 1: Create a DataPool with the data we want to retrieve.
    weatherdata = \
        DataPool(
           series=
            [{'options': {
               'source': MonthlyWeatherByCity.objects.all()},
              'terms': [
                'month',
                'houston_temp',
                'boston_temp']}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = weatherdata,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'boston_temp',
                    'houston_temp']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Weather Data of Boston and Houston'},
               'xAxis': {
                    'title': {
                       'text': 'Month number'}}})

    #Step 3: Send the chart object to the template.
    return render_to_response('sample.html', {'weatherchart': cht})