from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
from scrapy.crawler import Settings as settings
class SpidertutorialPipeline(object):

    def __init__(self):

        dbargs = dict(
            host = '127.0.0.1' ,
            db = 'spiderdb',
            user = 'root', #replace with you user name
            passwd = 'lkmn159357', # replace with you password
            charset = 'utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode = True,
            )    
        self.dbpool = adbapi.ConnectionPool('MySQLdb',**dbargs)


    '''
    The default pipeline invoke function
    '''
    def process_item(self, item,spider):
        res = self.dbpool.runInteraction(self.insert_into_table,item)
        return item
    def insert_into_table(self,conn,item):
        conn.execute('insert into tmp(title,category,summary,pub_time,author,scan) values(%s,%s,%s,%s,%s,%s)', (item['title'],item['category'],item['summary'],item['pub_time'],item['author'],item['scan']))