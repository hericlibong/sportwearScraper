# Nike, Adidas Scraper


### Presentation

The script of this repo written with the Scrapy framework allows to collect data from Nike and Adidas websites via their unofficial API.

![adidas](medias/C-10241__19959.jpeg) ![nike](medias/56b6b51994438bea310897f5368326d4-d2xgldc.png)

### usage

- Create a folder directory
- Clone the repo
- Create a virtual env

```shell
python3.10 -m venv venv

```
- Install Scrapy

```shell
python3.10 -m pip install scrapy

```

- go to the spider folder and the choosen file, exemple : 

```shell
scrapy runspider adidas.py
```
to export data run : 

```shell
scrapy runspider adidas.py -o data.json or data.csv
````




