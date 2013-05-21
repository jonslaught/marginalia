import snippets
import frequency
import time
import json

#now = int(time.time())
now = '5-16'
#ARTICLES = ['davidsimon','googlemaps','kevinkelly','mlkdream','stevejobs','whymilk']
#ARTICLES = ['mlkdream','stevejobs','whymilk']
ARTICLES = ['davidsimon','kevinkelly','stevejobs','whymilk']
#ARTICLES = ['mlkjail','lizlemon','socialnetwork','benham','klout','future','davidsimon','kevinkelly','googlemaps','howto']
GET_FREQ = True


for source in ARTICLES:
	print 'Reading %s' % source

	# Open a file, load into an article
	input = open('../data/articles/%s.html' % source,'r')
	a = snippets.Article(input.read())

	# Break it into snippets
	a.snip()

	# Save marked file
	output = open('../data/%s_%s_marked.html' % (now,source),'w')
	output.write(a.html)
	output.close()

	output = open('../data/%s_%s_snippets.js' % (now,source),'w')
	output.write(json.dumps(a.snippets,indent=4))
	output.close()

	if GET_FREQ:

		# Measure frequency
		freq = frequency.get_result_counts(a.snippets,max_calls=9999999,pause=0)

		# Save frequency to file
		output = open('../data/%s_%s_counts.js' % (now,source),'w')
		output.write(json.dumps(freq,indent=4))
		output.close()