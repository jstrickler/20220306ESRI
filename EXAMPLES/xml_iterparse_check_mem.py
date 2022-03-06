#!/usr/bin/env python
from lxml.etree import iterparse
from memorychecker import MemoryChecker

def main():
    doc = iterparse("../BIG_DATA/pubmed19n0001.xml", tag='PubmedArticle')  # <1>

    mem_checker = MemoryChecker()  # <2>

    for i, (event, element) in enumerate(doc, 1):  # <3>
        year_completed = element.findtext('.//DateCompleted/Year')  # <4>
        month_completed = element.findtext('.//DateCompleted/Month')
        clear_element(element)
        current_mem_use = mem_checker() # <5>

        print("{:5d}. {}/{} {}".format(i, month_completed, year_completed, current_mem_use))

    print("Total count: {}".format(i))

def clear_element(element):
    element.clear()  # <6>
    while element.getprevious() is not None:  # <7>
        del element.getparent()[0]  # <8>

if __name__ == '__main__':
    main()
