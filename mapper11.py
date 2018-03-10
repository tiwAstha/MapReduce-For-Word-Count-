import sys
import re

for n in sys.stdin:
    n = n.strip()
    words=re.split(" |\"|! |!|\?|, |\.|,|'|\(|\)|--|\*",n)
    for word in words:
	word=word.lower();
        if word != "":
        	print '%s\t%s' % (word, 1)




