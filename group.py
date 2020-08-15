from operator import itemgetter
from itertools import groupby

lki = [["A",0], ["B",1], ["C",0], ["D",2], ["E",2]]
lki.sort(key=itemgetter(1))

print(lki)
glo = [[x for x,y in g]
       for k,g in  groupby(lki,key=itemgetter(1))]

print(glo)
