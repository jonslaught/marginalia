import snippets
import frequency
import time
import json

now = int(time.time())
ARTICLE = 'howto'

# Open a file, load into an article
input = open('../data/articles/%s.html' % ARTICLE,'r')
a = snippets.Article(input.read())

# Break it into snippets
html, snippets = a.snip()

# Save marked file
output = open('../data/%s_%s_marked.html' % (now,ARTICLE),'w')
output.write(a.html)
output.close()

output = open('../data/%s_%s_snippets.json' % (now,ARTICLE),'w')
output.write(json.dumps(a.snippets,indent=4))
output.close()

# Measure frequency
freq = frequency.get_result_counts(a.snippets,max_calls=50,pause=0.5)

# Save frequency to file
output = open('../data/%s_%s_counts.json' % (now,ARTICLE),'w')
output.write(json.dumps(freq,indent=4))
output.close()