#!/usr/bin/python2

# Trying to prepare for python3
from sys import version_info as vi
if vi[0] ==3:
    ifilter = filter
    izip = zip
    imap = map
else:
    from itertools import imap, ifilter, izip

from re import split, sub, compile
from itertools import chain
from pprint import pprint
from fileinput import input

backticks=compile('`')
metadata=compile('((?:#[^\n]+\n)+)')
meta_lines=compile('# ([^\n]+)\n')
meta_keywords=compile('((?:[A-Z][^: ]+)):')
sql_lines=compile('([^;]+);')
newline=compile('\n')

def pair_list(l):
    tl=[]
    for x,y in izip(l[0::2],l[1::2]):
        tl.append((x,y))
    return tl

def hash_list(l):
    h={}
    for x,y in izip(l[0::2],l[1::2]):
        h[x]=y
    return h

header=1
slow_log_bulk=''
for line in input():
    if header==1 and line[0]=='#':
        header=0
    if header==0:
        slow_log_bulk+=backticks.sub('',line)

metadata_and_data_grouped = pair_list(filter(lambda x : x!='' and x !='\n', metadata.split(slow_log_bulk)))

slow_log_dict=[]
for i in metadata_and_data_grouped:
    slow_log_dict.append(
        hash_list(
            map(str.strip,
                ifilter(
                    lambda x : x!='',
                    chain.from_iterable(
                        imap(lambda x : meta_keywords.split(x),
                        ifilter(
                            lambda x : x!='' and x!='\n' ,
                            meta_lines.split(i[0]))))))))
    slow_log_dict[-1].update({'queries':
        map(str.strip,
            ifilter(
                lambda x : x!='' and x!='\n' and x!=' ',
                    sql_lines.split(
                        newline.sub(' ',i[1]))))})
#    slow_log_dict[-1].pop('QC_hit',None)

map(lambda x : pprint(x),slow_log_dict)
