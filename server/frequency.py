import re
import urllib, urllib2
import random, time

# Count the frequency of each snippet

def get_result_counts(snippets,pause=1,max_calls=1000):

	freq = {}

	for id, s in snippets.items()[:max_calls]:

		# Normalize into a query
		normalized = re.sub(r'[^\w\s]',' ',s['text'])
		query = urllib.quote_plus('"%s"' % normalized)

		# Load page
		burl = 'https://www.bing.com/search?q=%s' % query
		page = urllib2.urlopen(burl).read()

		# Parse out result count
		RE_RESULTS = r'<span class="sb_count" id="count">(?P<results>.*) results</span>'
		results_string = re.search(RE_RESULTS,page).group('results')
		result_count = int(results_string.replace(',',''))

		# Save results
		freq[id] = result_count

		# Print updates
		print [id,result_count,normalized]

		# Politeness
		time.sleep(pause + random.random()) # in seconds


	return freq

