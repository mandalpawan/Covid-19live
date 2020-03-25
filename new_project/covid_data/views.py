from django.shortcuts import render
from covid.api import CovId19Data



# Create your views here.
def home(request):
    api = CovId19Data(force=True)
    res = api.get_stats()

    res = api.get_all_records_by_country()
    country = []
    confirm = []
    death = []
    recover = []
    for i in res:
        #print(res[i]['label'],"          ",res[i]['confirmed'])
        country.append(res[i]['label'])
        country.append(res[i]['confirmed'])
        country.append(res[i]['deaths'])
        country.append(res[i]['recovered'])
    print(country)
    print(confirm)
    print(death)
    print(recover)
    return render(request,'index.html',{'country':country,'confirm':confirm,'death':death,'recover':recover})