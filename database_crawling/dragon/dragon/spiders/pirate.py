import scrapy
from dragon.items import Torrent
from scrapy.selector import HtmlXPathSelector

#
# https://github.com/mlakkadshaw/PirateDownloader/tree/master/torrentcrawler
#

	
class Pirate(scrapy.Spider):
	name = "pirate"
	allowed_domains = ["thepiratefilmestorrent.com"]
	start_urls = [ "http://www.thepiratefilmestorrent.com/dbsuper-hdtv-720p-legendado-torrent/" ]
		
	def parse(self, response):
		if response.status != 404:
			torrent = Torrent()
			hxs = scrapy.Selector(response)
			#torrent['title'] = hxs.xpath('//title/text()').extract()
			torrent['link'] = hxs.xpath("//strong/a[contains(@href, 'magnet:')]/@href").extract()
			return torrent