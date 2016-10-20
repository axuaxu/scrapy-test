from craigslist import CraigslistHousing

cl = CraigslistHousing(site='sfbay',area='sfc',category='apa', filters={'max_price':2000,'min_price':1000})

results = cl.get_results(sort_by='newest', geotagged=True,limit=20)

for result in results:
    print result
