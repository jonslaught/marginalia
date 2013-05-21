import re
import urllib, urllib2, httplib
import random, time

# Count the frequency of each snippet

def get_result_counts(snippets,pause=1,max_calls=1000):

	freq = {}

	for id, s in snippets.items()[:max_calls]:

		# Normalize into a query
		#normalized = re.sub(r'[^\w\s]','',s['text'])

		normalized = re.sub(r'\s',' ',s['text'])
		normalized = re.sub(r'[\"]','',normalized)

		query = urllib.quote_plus('"%s"' % normalized)

		# Load page
		burl = 'https://www.bing.com/search?q=%s' % query
		
		try:
			f = urllib2.urlopen(burl)
			page = f.read()
			f.close()
		except httplib.IncompleteRead as e:
			page = e.partial
			f.close()

		# Parse out result count
		RE_RESULTS = r'<span class="sb_count" id="count">(?P<results>.*) results</span>'
		match = re.search(RE_RESULTS,page)

		
		if re.search(r'No results found',page):
			result_count = 0
		elif match:
			results_string = match.group('results')
			result_count = int(results_string.replace(',','')) 
		else:
			# Probably no results -- but should really investigate in the future
			print ['Error finding result count',burl,page]
			f.close()
			continue

		# Save results
		freq[id] = result_count

		# Print updates
		print [id,result_count,normalized]

		# Politeness
		time.sleep(pause + random.random()) # in seconds


	return freq

