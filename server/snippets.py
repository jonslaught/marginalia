from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag
import re

# Break an HTML file into snippets of text

class Article(object):

	def __init__(self,raw_html):
		self.raw_html = raw_html
		self.soup = BeautifulSoup(raw_html)
		self.snippets = {}

	def snip(self):

		self.soup = self.find_snippets_in_tag(self.soup)
		self.html = str(self.soup)
		return self.html, self.snippets

	# Decides if a snippet is worth including
	def is_worth_snipping(self,text):
		return len(text.strip()) > 30

	# Marks a spot within an HTML string with snippet open/close tags
	# Also saves the snippet
	def mark_snippet(self,in_html,start,end):

		contents_html = in_html[start:end]
		contents_text = BeautifulSoup(contents_html).text

		if self.is_worth_snipping(contents_text):

			id = len(self.snippets)
			#start_marker = '{%s{' % id
			#end_marker = '}%s}' % id
			start_marker = '<mark id="%s">' % id
			end_marker = '</mark>'
			
			self.snippets[id] = {
				'html': contents_html,
				'text': contents_text
			}

			newhtml = in_html[:start] + start_marker + in_html[start:end] + end_marker + in_html[end:]
			return self.snippets[id], newhtml

		else:
			return None, in_html

	# Mark snippets in a string of text
	def find_snippets_in_text(self,text):
	
		RE_BOUNDARY = r'(?P<punc>[.!?]+)(?P<space>\s+)'

		last = 0
		ranges = []

		for match in re.finditer(RE_BOUNDARY,text):
			
			# End at the period, start after the spacing
			end = match.end('punc')
			start_from = match.end('space')
			ranges += [(last,end)]
			last = start_from

		ranges += [(last,len(text))] # go to the end


		# From the end, start marking snippets
		# Keep updating text variable as we go
		for start, end in reversed(ranges):
			snippet, text = self.mark_snippet(text,start,end)

		return text

	# Recursively mark snippets in an HTML tag
	def find_snippets_in_tag(self,tag):

		text_block = ""
		new_contents = []

		for child in tag.contents:

			# P tag
			if type(child) is Tag and child.name in ['p','br','blockquote','div']:

				# Submit the previous text block
				#snippets += self.snippets_from_text(textblock)
				new_contents.append(BeautifulSoup(self.find_snippets_in_text(text_block)))
				text_block = ""

				# Then add these
				new_contents.append(self.find_snippets_in_tag(child))
			
			# Other tag, or string
			else:

				# Build up the current snippet
				text_block += str(child)

		# If there's anything left
		if text_block:
			new_contents.append(BeautifulSoup(self.find_snippets_in_text(text_block)))
		
		#print ['newcontents',newcontents]
		tag.contents = new_contents
		return tag