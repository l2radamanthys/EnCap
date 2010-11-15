#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    simple parser para extraer los links de los diferentes sitios de
    descargas de archivos particionados, para usarse en el jdownloader
"""


from sgmllib import SGMLParser
import urllib
import sys


DOW_SITES = [
    'megaupload.com',
    'rapidshared.com',
]


def is_dow_site(url):
    for tag in DOW_SITES:
        if tag in url:
            return True
    return False


class URLParser(SGMLParser):
    def __init__(self):
        SGMLParser.__init__(self)
        self.url = ''
        self.urls = []


    def reset(self):
        SGMLParser.reset(self)
        self.url = ''
        self.urls = []


    def start_a(self, attrs):
        for tag, value in attrs:
            tag = tag.lower()
            if tag == 'href':
                #self.urls.append(value)
                if is_dow_site(value):
                    self.urls.append(value)


    def handle_data(self, text):
        text = text.replace('http://', ' http://')
        data = text.split()
        for value in data:
            if is_dow_site(value):
                self.urls.append(value)


def main():
    print """

        ----------------------------------------
        EnCap (Capturador de enlace de Descarga)
        Version: 0.0.2 (Alpha)
        ----------------------------------------

    """
    url = 'http://www.taringa.net/posts/juegos/1123319/Lineage-2-Kamael-Megaupload-40-partes.html'
    if len(sys.argv != 2):
        print "argumentos invalidos\nusar encap www.pagina_a_buscar.com"
        sys.exit(-1)

    #url = sys.argv[1]
    sock = urllib.urlopen(url)
    data = sock.read()
    sock.close()

    mi_parser = URLParser()
    mi_parser.feed(data)
    urls = mi_parser.urls

    f = open('urls.txt', 'w')
    for url in mi_parser.urls:
        f.write('%s\n' %url)
    f.close

    print 'analisis completado..'

if __name__ == '__main__':
    main()


