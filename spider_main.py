#coding=utf8
import url_manager, html_downloader, html_outputer, html_parser
class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
    def craw(self,root_url,total_num = 20):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print "craw %d : %s"%(count,new_url)
                html_cont =self.downloader.download(new_url)
                #print html_cont
                #print "download_ok"
                new_urls, new_data = self.parser.parse(new_url,html_cont)
                #print new_data['title']
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == total_num:
                    break
                count = count + 1
            except:
                print "craw_failed"
        self.outputer.output_html()

if __name__ == "__main__":
    root_url = raw_input("Please input the root url:")
    try:
        total_num = int(raw_input("Please input how many pages you want to crawl(dedault value is 20):"))
    except:
        total_num = 20
    obj_spider = SpiderMain()
    obj_spider.craw(root_url,total_num)