# Create your views here.
from chartit import DataPool, Chart, PivotDataPool, PivotChart
from graphs.scrum.models import SurveyResponse
from django.shortcuts import render_to_response
from django.db.models import Count

def scrum_chart_view(request):
    #Step 1: Create a DataPool with the data we want to retrieve.
    weatherdata = \
        DataPool(
           series=
            [{'options': {
               'source': SurveyResponse.objects.all()},
              'terms': [
                'role',
                'scrum_1',
                'scrum_2']}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = weatherdata,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'role': [
                    'scrum_1',
                    'scrum_2']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Usage of Scrum per roles'},
               'xAxis': {
                    'title': {
                       'text': 'Role'}}})

    #Step 1: Create a PivotDataPool with the data we want to retrieve.
    rainpivotdata = \
        PivotDataPool(
           series =
            [{'options': {
               'source': SurveyResponse.objects.all(),
               'categories': ['scrum_1'],
               'legend_by': 'role'},
              'terms': {
                'avg_rain': Count('scrum_1')}}
             ])

    #Step 2: Create the PivotChart object
    rainpivcht = \
        PivotChart(
            datasource = rainpivotdata,
            series_options =
              [{'options':{
                  'type': 'column',
                  'stacking': True},
                'terms':['avg_rain']}],
            chart_options =
              {'title': {
                   'text': 'Rain by Month in top 3 cities'},
               'xAxis': {
                    'title': {
                       'text': 'Value'}}})

    #Step 3: Send the PivotChart object to the template.
    return render_to_response('scrum_graphs.html', {'weatherchart': rainpivcht})