#!/usr/anim/bin/pypix

#-----------------------------------------------------------------------
#
# run something like this to generate the keyword class:
#
# the production orapig.py is:
#     /usr/anim/modsquad/orapig.py
#
#-----------------------------------------------------------------------

def X(s):
    print
    print '-'*72
    print s
    print '-'*72

def capitalized(curs):
    """demonstrating an application-specific api call"""
    curs.execute('select unique keyword from keywords order by keyword')
    return [row[0].capitalize() for row in curs.fetchall()]

import pixardb
import keyword
from pprint import pprint

X('connect to the database')
conn = pixardb.connection()
curs=conn.cursor()

X('instantiate a keyword object see its methods')
k=keyword.Keyword(curs)
pprint(dir(k))

X('autogenerated doc string')
print k.__doc__

X('autogenerated doc string for a method')
print k.add.__doc__

X('add a keyword')
print k.add(22,'blue')

X('add some keywords using the vectorizing procedure')
k.add_V([
    [21,'orange'],
    [22,'violet'],
    [23,'white'],
    [24,'black']
])

# speculating about adding this form of parameter, opinions welcomed
#k.add_V2([
#    {'k':22,'v':'orange'},
#    {'k':22,'v':'violet'},
#    {'k':22,'v':'white'},
#    {'k':22,'v':'black'}
#])


X('list all the keywords')
iter=k.all_words()
for r in iter:
    print r[0]

X('list all the keywords, list consing version (good for xml-rpc, app server')
allwords=k.all_words_L()
print allwords

X('list the keywords for asset 22')
iter=k.get_keywords2(22)
for r in iter:
    print r[0]

X('delete a keyword')
print k.delet(22,'red')

X('call an application specific api')
print capitalized(curs)

X('escape to sql')
curs.execute('select count(*) from keywords where id=:x',x=22);
print curs.fetchone()

# commit your changes, if you like
# curs.commit()

conn.close()
