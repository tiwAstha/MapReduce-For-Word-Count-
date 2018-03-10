from operator import itemgetter
import sys

thisWord = None
thisCount = 0
word = None
for n in sys.stdin:
    n = n.strip()
    try:
        count = int(count)
    except ValueError:
        continue
    if thisWord == word:
        thisCount= thisCount+count
    else:
        if thisWord:
            print '%s\t%s' % (thisWord, thisCount)
        thisCount = count
        thisWord = word
if thisWord == word:
    print '%s\t%s' % (thisWord, thisCount)

