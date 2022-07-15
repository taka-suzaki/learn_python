import xml.sax
import xml.sax.handler
import sys

class Handler(xml.sax.handler.ContentHandler):
	def startElementNS(self, name, qname, attrs):
		print ("Start:", name, qname, attrs)

	def endElementNS(self, name, qname):
		print( "End:", name, qname)
	
	def characters(self, content):
		print( "character:" + content)
		return

def main():
	parser = xml.sax.make_parser()
	parser.setContentHandler(Handler())
	parser.setFeature(xml.sax.handler.feature_namespaces, True)
	parser.parse(sys.stdin)
	return
	
if __name__=="__main__":
	main()