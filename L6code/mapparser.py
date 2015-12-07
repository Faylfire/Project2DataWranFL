#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Your task is to use the iterative parsing to process the map file and
find out not only what tags are there, but also how many, to get the
feeling on how much of which data you can expect to have in the map.
The output should be a dictionary with the tag name as the key
and number of times this tag can be encountered in the map as value.

Note that your code will be tested with a different data file than the 'example.osm'
"""
import xml.etree.ElementTree as ET
import pprint

def count_tags(filename):
    i = 0
    #tagSet = set()
    tagDict = {}
    for event, elem in ET.iterparse(filename):
        #print 'Event: ', event, '\nElem: ', elem, '\nTag: ', elem.tag
        #tagSet.add(elem.tag)
        if tagDict.has_key(elem.tag):
            tagDict[elem.tag] += 1
        else:
            tagDict[elem.tag] = 1
        
        '''        
        i += 1
        if i > 4:
            break
        '''
    #print tagSet
    #print tagDict
    return tagDict

def test():

    tags = count_tags('example.osm')
    pprint.pprint(tags)
    assert tags == {'bounds': 1,
                     'member': 3,
                     'nd': 4,
                     'node': 20,
                     'osm': 1,
                     'relation': 1,
                     'tag': 7,
                     'way': 1}

    

if __name__ == "__main__":
    test()