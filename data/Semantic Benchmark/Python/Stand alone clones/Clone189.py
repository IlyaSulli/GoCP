def _extract_links(self, selector, response_url, response_encoding, base_url) :
	links = []
	for el, attr, attr_val in self._iter_links(selector._root) :
		attr_val = urljoin(base_url, attr_val.strip())
		url = self.process_attr(attr_val)
		if url is None :
			continue
		if isinstance(url, unicode) :
			url = url.encode(response_encoding)
		url = urljoin(response_url, url)
		link = Link(url, _collect_string_content(el) or u'',
		nofollow = True if el.get('rel') == 'nofollow' else False)
		links.append(link)
	return unique_list(links, key = lambda link : link.url) if self.unique else links


def _extract_links(self, response_text, response_url, response_encoding, base_url = None) :
	if base_url is None :
		base_url = urljoin(response_url, self.base_url) if self.base_url else response_url
	clean_url = lambda u : urljoin(base_url, remove_entities(clean_link(u.decode(response_encoding))))
	clean_text = lambda t : replace_escape_chars(remove_tags(t.decode(response_encoding))).strip()
	links_text = linkre.findall(response_text)
	urlstext = set([(clean_url(url), clean_text(text)) for url, _, text in links_text])
	return [Link(url, text) for url, text in urlstext]

