import re , os ,sys
documents = []
searches = {}
title_search = re.compile(r'(title:)(?P<title>(.*?\n\s*\n))', re.IGNORECASE | re.DOTALL)
author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)
def loadDocuments(directory):
	for fl in (os.listdir(directory)):  #for each item that appears in the directory
	    if fl.endswith('.txt'):       #if it's a text file
	        with open(os.path.join(directory, fl), 'r') as f:         #open the file as f
	            documents.append(f.read())   
def loadSearches():
	for kw in sys.argv[2:]: 
	  searches[kw] = re.compile(r'\b' + kw + r'\b', re.IGNORECASE)
def printOutput():
	for i, doc in enumerate(documents):
	  title = re.search(title_search, doc).group('title')
	  author = re.search(author_search, doc)
	  translator = re.search(translator_search, doc)
	  illustrator = re.search(illustrator_search, doc)
	  if author: 
	    author = author.group('author')
	  if translator:
	    translator = translator.group('translator')
	  if illustrator:
	    illustrator = illustrator.group('illustrator')
	  print "***" * 25
	  print "Here's the info for doc {}:".format(i)
	  print "Title:  {}".format(title)
	  print "Author(s): {}".format(author)
	  print "Translator(s): {}".format(translator)
	  print "Illustrator(s): {}".format(illustrator)
	  print "Here is the count of the keywords you searched for:"
	  for search in searches:
	    print "\"{0}\":{1}".format(search, len(re.findall(searches[search], doc)))
	  print "\n"
def main(argv=sys.argv):
	try:
		if(len(argv)>1):
			loadDocuments(argv[1])
			loadSearches()
			printOutput()
		else:
			print "Usage: document_tagger_final.py path searchstring"
	except Exception as e:
		print e
if __name__ == '__main__':
	main()