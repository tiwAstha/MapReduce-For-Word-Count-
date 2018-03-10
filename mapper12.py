import sys
import re

for n in sys.stdin:
    n = n.strip()
    words=re.split(' |; |\?|, |\"|\*|,|\.|!',n)
    for w in words:
	w=w.lower()
        if w != "":
            if (w == w[::-1] ):
                print '%s\t%s' % (w, 1)





