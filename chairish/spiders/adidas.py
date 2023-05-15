import scrapy
import json


class AdidasSpider(scrapy.Spider):
    name = "adidas"
    allowed_domains = ["adidas.com"]
    start_urls = ["https://www.adidas.com/api/plp/content-engine?sitePath=us&query=men-shoes&start=48"]

    def parse(self, response):
        parse_json = json.loads(response.body)
        data = parse_json['raw']['itemList']['items']
        for item in data:
            productId = item['productId']
            modelId = item['modelId']
            displayName = item['displayName']
            category = item['category']
            sport = item['sport']
            price = item['price']
            salePrice = item['salePrice']
            salePercentage = item['salePercentage']
            isFlash = item['isFlash']
            onlineFrom = item['onlineFrom']
            rating = item['rating']
            ratingCount = item['ratingCount']
            rawlink = item['link']
            link = 'https://www.adidas.com'+rawlink
            image1 = item['image']['src']
            try :
                image2 = item['secondImage']['src']
            except :
                image2 = None


            yield {
                'productId' : productId,
                'modelId' : modelId,
                'displayName':displayName,
                'category' : category,
                'sport': sport,
                'price' : price,
                'salePrice': salePrice,
                'salePercentage': salePercentage,
                'isFlash' : isFlash,
                'onlineFrom' : onlineFrom,
                'rating' : rating,
                'ratingCount' : ratingCount,
                'link' : link,
                'mainImage' : image1, 
                'secondImage': image2

            }
        

        #pagination
        items = [i for i in range(0, 1557, 48)]
        for num_item in items :
            url = f'https://www.adidas.com/api/plp/content-engine?sitePath=us&query=men-shoes&start={num_item}'
            yield scrapy.Request(url=url, callback=self.parse)


   