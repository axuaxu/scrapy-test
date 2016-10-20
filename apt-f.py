from craigslist import CraigslistHousing

cl = CraigslistHousing(site='sfbay',area='sfc',category='roo', filters={'max_price':3000,'private_room':True})

results = cl.get_results(sort_by='newest', geotagged=True,limit=50)

for result in results:
    print result
