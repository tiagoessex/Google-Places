
Version: 0.0.1

# Description
* If places are founded, returns a list of jsons containing all the entities/places. If not, returns a single json with **'status': 'ZERO_RESULTS'**.
* In case of incorrect usage (e.g.: incorrect arguments, invalid key) or some other catastrophic event, a _RuntimeError_ or a _Exception_ will be throwed


# Requirements
* Python 3.7.x


# Fields
* name
* address
* latitude
* longitude
* place_id
* global_code
* types (list of types associated with each entity. See: https://developers.google.com/places/web-service/supported_types)
* open_now (true|false)
* rating

# Example

```python


import googleplaces

try:
	a = googleplaces.getAllPlaces(
			key = 'xxxxxxxxxxxxxxxxxxxxxx', 
			latitude = 41.146057, 
			longitude = -8.605268, 
			radius = 500, 
			type='restaurant',
			total = 10)

	for i in a:
		print (i)
		print ("\n\n")

except Exception as e:
	print (str(e))


```

# Notes: 
* Only uses **Google** services.
* Each call requires one API call.
* Máx number of returned places per API call: 20
* If total > 20, then there's going to be a 2 seconds delay, for each API call. If not, a **INVALID_REQUEST** would be throwed.
