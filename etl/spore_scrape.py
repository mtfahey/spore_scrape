import requests

#an example of the form
example = "http://static.spore.com/static/image/501/091/312/501091312194_lrg.png"

#root directory for images
root = "http://static.spore.com/static/image/"

#cycle through the 12-digit id starting at 5 billion
#500000000000
#502000000000
for this_id in range(500000000000, 502000000000):
	this_id = str(this_id)

	#get the directories from the id
	dir_1 = this_id[:3]
	dir_2 = this_id[3:6]
	dir_3 = this_id[6:9]
	#make full link
	link = root+dir_1+"/"+dir_2+"/"+dir_3+"/"+this_id+"_lrg.png"

	print(link)

	#get images
	#../data/processed/"+
	image = requests.get(link)
	file = open(this_id+"_lrg.png", "wb")
	file.write(image.content)
	file.close()