#!/usr/bin/env python
from lxml.etree import iterparse


def main():
    doc = iterparse("../BIG_DATA/pubmed19n0001.xml", tag='PubmedArticle')  # <1>

    for i, (event, element) in enumerate(doc, 1):  # <2>
        article_title = element.findtext('.//ArticleTitle')   # <3>
        year_completed = element.findtext('.//DateCompleted/Year')  # <3>
        month_completed = element.findtext('.//DateCompleted/Month')  # <3>
        clear_element(element)  # <4>
        print("{}/{} {}".format(month_completed, year_completed, article_title[:70]))

    print("Total count: {}".format(i))


def clear_element(element):
    element.clear()  # <5>
    while element.getprevious() is not None:  # <6>
        del element.getparent()[0]  # <7>


if __name__ == '__main__':
    main()
