import urllib.request
from bs4 import BeautifulSoup
import re
import webbrowser


# Html Scrapping using Beautiful Soup
def html_parser(link):
    count = 0
    headers = {}

    # User-Agent header is done to avoid exceptional error if website blocks any bot entry.
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko)" \
                            " Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(link, headers=headers)
    source = urllib.request.urlopen(req)
    sourcedata = str(source.read())
    souped_data = BeautifulSoup(sourcedata, 'html.parser')
    for link in souped_data.findAll('a', {'href': re.compile("watch")}):
        if not re.findall(r'https://', link.get('href')):
            firstlink = link.get('href')

            count += 1
            browser(firstlink)
        if count == 1:
            break


def browser(firstlink):
    firstlink = 'https://www.youtube.com' + firstlink
    webbrowser.open(firstlink)
