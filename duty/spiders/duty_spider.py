import scrapy
from duty.items import DutyItem
import os 
from xlutils.copy import copy 
import xlrd as ExcelRead
import string

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://10.58.52.202:8080/cat/r/t?date=2017061709&ip=All&step=-1&ip=All&queryname=sendSms&domain=loom&type=PigeonService",

        "http://10.58.52.202:8080/cat/r/t?ip=All&queryname=registerUnifyUser&domain=userCenter&type=PigeonService",
        "http://10.58.52.202:8080/cat/r/t?ip=All&queryname=regUser&domain=userCenter&type=PigeonService",
        
        "http://10.58.52.202:8080/cat/r/t?ip=All&queryname=IUserLoginFacade.doLogin&domain=userCenter&type=PigeonService",
        "http://10.58.52.202:8080/cat/r/t?ip=All&queryname=ISNSLoginFacade.doSNSLogin&domain=userCenter&type=PigeonService",
        "http://10.58.52.202:8080/cat/r/t?ip=All&queryname=getItemById&domain=userCenter&type=PigeonService",
        "http://10.58.52.202:8080/cat/r/t?ip=All&queryname=getUserByIdFromCache&domain=sso&type=PigeonService",
        "http://10.58.52.202:8080/cat/r/t?ip=All&queryname=saveUserToCacheFonInner&domain=sso&type=PigeonService",

        "http://10.58.52.202:8080/cat/r/t?ip=All&queryname=.changeGomedo&domain=memberGomedo&type=PigeonService",
        "http://10.58.52.202:8080/cat/r/t?ip=All&queryname=getUsableGomedo4Shopping&domain=memberGomedo&type=PigeonService",

        "http://10.58.52.202:8080/cat/r/t?ip=All&queryname=getSecondaryAddress&domain=userBase&type=PigeonService",
        "http://10.58.52.202:8080/cat/r/t?ip=All&queryname=getGomeProfileUserInfoById&domain=userBase&type=PigeonService"
    ]
    def parse(self, response):
        for sel in response.xpath('//div[re:test(@class, "report")]/table[re:test(@class, "table")]'):
            file_name='D:\\example.xls'
            r_xls = ExcelRead.open_workbook(file_name) 
            r_sheet = r_xls.sheet_by_index(0) 
            rows = r_sheet.nrows 
            item = DutyItem()
            if rows==5:
                item['interfaceName'] = sel.xpath('tr[re:test(@class, "right")][3]/td[1]/text()').extract()
                item['total'] = sel.xpath('tr[re:test(@class, "right")][3]/td[2]/text()').extract()
                item['average'] = sel.xpath('tr[re:test(@class, "right")][3]/td[8]/text()').extract()
                item['line'] = sel.xpath('tr[re:test(@class, "right")][3]/td[9]/text()').extract()
                item['qps'] = sel.xpath('tr[re:test(@class, "right")][3]/td[12]/text()').extract()
            else:
                item['interfaceName'] = sel.xpath('tr[re:test(@class, "right")][2]/td[1]/text()').extract()
                item['total'] = sel.xpath('tr[re:test(@class, "right")][2]/td[2]/text()').extract()
                item['average'] = sel.xpath('tr[re:test(@class, "right")][2]/td[8]/text()').extract()
                item['line'] = sel.xpath('tr[re:test(@class, "right")][2]/td[9]/text()').extract()
                item['qps'] = sel.xpath('tr[re:test(@class, "right")][2]/td[12]/text()').extract()
            w_xls = copy(r_xls) 
            sheet_write = w_xls.get_sheet(0)
            sheet_write.write(rows, 0, item['interfaceName'])
            sheet_write.write(rows, 1, item['total'])
            sheet_write.write(rows, 2, item['average'])
            sheet_write.write(rows, 3, item['line'])
            sheet_write.write(rows, 4, item['qps'])
            w_xls.save(file_name); 
            yield item