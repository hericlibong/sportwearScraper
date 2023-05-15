import scrapy
import json


class ChairishApiSpider(scrapy.Spider):
    name = "chairish_api"
    allowed_domains = ["nike.com"]
    start_urls = ['https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=356882BA56C3E2490567C01BB0E01850&country=us&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(US)%26filter%3Dlanguage(en)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(ce570103-cb83-4b62-97e2-ea80fb12f38f%2C0f64ecc7-d624-4e91-b171-b83a03dd8550)%26anchor%3D24%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24&language=en&localizedRangeStr=%7BlowestPrice%7D%20%E2%80%94%20%7BhighestPrice%7D']

    def parse(self, response):
        parse_json = json.loads(response.body)
        data = parse_json['data']['products']['products']
        for item in data:
            id = item['id']
            colorDescription = item['colorDescription']
            bestseller = item['isBestSeller']
            stock = item['inStock']
            nba = item['isNBA']
            nfl = item['isNFL']
            label = item['label']
            sustainable = item['isSustainable']
            image1 = item['images']['portraitURL']
            image2 = item['images']['squarishURL']
            currency = item['price']['currency']
            currentprice = item['price']['currentPrice']
            discounted = item['price']['discounted']
            employeedprice = item['price']['employeePrice']
            fullprice = item['price']['fullPrice']
            minimumadvertiseprice = item['price']['minimumAdvertisedPrice']
            productinstanceid = item['productInstanceId']
            producttype = item['productType']
            properties = item['properties']
            salesChannel = item['salesChannel']
            title = item['title']
            subtitle = item['subtitle'] 
            rawurl = item['url']
            url = rawurl.replace('{countryLang}/', '') 
            url = 'https://www.nike.com/' + url 


            

            yield {
                'id':id, 
                'colorDescription':colorDescription,
                'isBestSeller':bestseller,
                'inStock': stock,
                'isNBA': nba,
                'isNFL': nfl,
                'label' : label,
                'isSustainable' : sustainable,
                'portraitURL': image1,
                'squarishURL':image2,
                'currency':currency,
                'currentPrice' : currentprice,
                'discounted' : discounted,
                'employeePrice': employeedprice,
                'fullPrice': fullprice,
                'minimumAdvertisedPrice':minimumadvertiseprice,
                'productInstanceId': productinstanceid,
                'productType':producttype,
                'properties': properties,
                'salesChannel': salesChannel,
                'title': title,
                'subtitle': subtitle,
                'url': url

                
              }

        items = [i for i in range(0, 776, 24)]

        for anchor in items:
            url = 'https://api.nike.com/cic/browse/v2?queryid=products&anonymousId=356882BA56C3E2490567C01BB0E01850&country=us&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(US)%26filter%3Dlanguage(en)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(16633190-45e5-4830-a068-232ac7aea82c%2C0f64ecc7-d624-4e91-b171-b83a03dd8550)%26anchor%3D{}%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24&language=en&localizedRangeStr=%7BlowestPrice%7D%20%E2%80%94%20%7BhighestPrice%7D'.format(anchor)
            yield scrapy.Request(url= url, callback = self.parse)
            

       