from craigslist import CraigslistHousing

cl_h = CraigslistHousing(site='sfbay',area='sfc',category='roo',filters={'max_price':5000,'private_room':True})

for result in cl_h.get_results(sort_by='newest',geotagged=True):
    print result
