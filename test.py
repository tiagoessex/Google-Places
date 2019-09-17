
import googleplaces

print (googleplaces.__version__)

try:
	a = googleplaces.getAllPlaces(
			key = 'xxxxxxxxxxxxxxxxxxxxxxxx', 
			latitude = 41.146057, 
			longitude = -8.605268, 
			radius = 500, 
			type='restaurant',
			keywords=['sushi'],
			total = 20)

	for i in a:
		print (i)
		print ("\n\n")

	
	print (len(a))

except Exception as e:
	print (str(e))


