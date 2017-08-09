#coding:utf8
from bs4 import BeautifulSoup
import urlparse
import re
class HtmlParser(object):
    #"/html/gndy/jddy/
    def _get_new_urls(self,page_url,soup):
        new_urls = set()
        links = soup.find_all('a',href = re.compile(r"/html/gndy/jddy/"))
        #print page_url
        for link in links:
            new_url = link['href']
            #print new_url
            new_full_url = urlparse.urljoin(page_url,new_url)
            #print new_full_url
            new_urls.add(new_full_url)
        return new_urls


    #<dd class="lemmaWgt-lemmaTitle-title">
    def _get_new_data(self,page_url,soup):
        res_data = {}

        #read url
        #res_data['url'] = page_url

        #read movie_name
        try:
            title = soup.find('div',class_ = "bd3r").find("h1")
            res_data['title'] = title.get_text()
            print res_data['title']

            #read download_url
            download_url = soup.find('div',id ="Zoom").find("a")
            res_data['download_url'] = download_url['href'];
            #print res_data['download_url']
            return res_data
        except:
            return None

        
    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            print "Nothing is captured"
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='gb2312')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data