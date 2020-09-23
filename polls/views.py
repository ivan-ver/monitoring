from django.shortcuts import render
from polls.data_base import Database


def index(request):
    s1 = get_tables()
    return render(request, 'polls/main_page.html', s1)

def get_tables():
    result = {}
    with Database() as db:
        result['service1'] = db.get_services_info('service1')
        result['service2'] = db.get_services_info('service2')
        result['service3'] = db.get_services_info('service3')
    return result
