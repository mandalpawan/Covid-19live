from covid.api import CovId19Data

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
    confirm.append(res[i]['confirmed'])
    death.append(res[i]['deaths'])
    recover.append(res[i]['recovered'])
    print(res[i])

print(country)
print(confirm)
print(death)
print(recover)