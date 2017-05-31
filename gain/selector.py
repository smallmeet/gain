from lxml import etree

from pyquery import PyQuery as pq


class Selector:
    def __init__(self, rule, attr=None):
        self.rule = rule
        self.attr = attr

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, self.rule)

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.rule)

    def parse_detail(self, html):
        NotImplementedError('parse() should be implemented')


class Css(Selector):
    def parse_detail(self, html):
        d = pq(html)
        if self.attr is None:
            return d(self.rule)[0].text
        return d(self.rule).attr(self.attr, '')


class Xpath(Selector):
    def parse_detail(self, html):
        d = etree.HTML(html)
        if self.attr is None:
            return d.xpath(self.rule)[0].text
        return d.xpath(self.rule)[0].get(self.attr, '')