# coding:utf-8
from DataOutput import DataOutput
from HtmlDownloader import HtmlDownloader
from HtmlParsert import HtmlParsert
from URLManager import UrlManager

import pymongo
import keyboard

class SpiderMan(object):
    def __init__(self):
        self.downloader = HtmlDownloader()
        self.parser = HtmlParsert()
        self.output = DataOutput()
        self.manager = UrlManager()

    def crawl(self, root_url):
        self.manager.add_new_url(root_url)

        while (self.manager.has_new_url() and self.manager.old_url_size() < 10):
            try:
                new_url = self.manager.get_new_url()
                html = self.downloader.download(new_url)
                new_urls, data = self.parser.parser(new_url, html)
                self.manager.add_new_urls(new_urls)
                self.output.store_data(data)
                print 'crawl %s 个链接' % self.manager.old_url_size()
            except Exception, e:
                print 'crawl fail.'
        self.output.output_html()


class MongoDemo(object):
    def createDB(self):
        server = pymongo.MongoClient()
        database = server['Database']
        return database

    def createCollection(self, database):
        collection = database['Collection']
        return collection

    def insertDoc(self, database, files):
        collection = database['Collection']
        infor_id = collection.insert(files)
        print infor_id


if __name__ == '__main__':
    spider_man = SpiderMan()
    spider_man.crawl("http://baike.baidu.com/view/284853.htm")

    
