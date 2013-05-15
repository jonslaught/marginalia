import re
import urllib, urllib2
import random, time

# Count the frequency of each snippet

def get_result_counts(snippets,pause=1,max_calls=1000,logtext='frequency_log.txt'):

	freq = {}
	t = open(logtext,'a')

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

		# Print to file
		print [id,result_count,s['text']]
		print >> t, '%s|%d|%s' % (id,result_count,s['text'])
		t.flush()

		# Politeness
		time.sleep(pause + random.random()) # in seconds


	t.close()
	return freq

