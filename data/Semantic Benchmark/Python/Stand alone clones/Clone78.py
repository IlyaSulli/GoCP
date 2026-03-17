def parse(self, response) :
	log.msg("Begin Parsing", level = log.INFO)
	log.msg("Response from: %s" % response.url, level = log.INFO)
	hxs = HtmlXPathSelector(response)
	sites = hxs.select("//*[@id='moduleData8460']")
	items = response.meta ['items']
	for site in sites :
		item = MlboddsItem()
		item ['header'] = site.select('//div[@class="scoreboard-bar"]//h2//span[position()>1]//text()').extract()
		item ['game1'] = site.select('/*//table[position()=1]//tr//td[@class="tbl-odds-c2"]//text()').extract()
		items.append(item)
	if self.other_urls :
		return Request(self.other_urls.pop(0), meta = {'items' : items})
	return items


def parse(self, response) :
	hxs = HtmlXPathSelector(response)
	sites = hxs.select('//div[@id="col_3"]//div[@id="module3_1"]//div[@id="moduleData4952"]')
	items = []
	for site in sites :
		item = MlboddsItem()
		item ['header'] = site.select('//div[@class="scoreboard-bar"]//h2//span[position()>1]//text()').extract()
		item ['game1'] = site.select('/*//table[position()=1]//tr//td[@class="tbl-odds-c2"]//text() | /*//table[position()=1]//tr//td[@class="tbl-odds-c4"]//text() | /*//table[position()=1]//tr//td[@class="tbl-odds-c6"]//text()').extract()
		items.append(item)
	return items

