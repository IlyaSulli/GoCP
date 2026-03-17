def pdf_to_text(url = None) :
	text = None
	pdf = requests.get(url)
	if pdf.ok :
		fp = StringIO(str(pdf.content, 'utf-8'))
		outfp = StringIO()
		rsrcmgr = PDFResourceManager()
		device = TextConverter(rsrcmgr, outfp, laparams = LAParams())
		process_pdf(rsrcmgr, device, fp)
		device.close()
		text = outfp.getvalue()
		outfp.close()
		fp.close()
	return text


def pdf_to_text(scraped_pdf_data) :
	from pdfminer.pdfinterp import PDFResourceManager, process_pdf
	from pdfminer.pdfdevice import PDFDevice
	from pdfminer.converter import TextConverter
	from pdfminer.layout import LAParams
	import StringIO
	fp = StringIO.StringIO()
	fp.write(scraped_pdf_data)
	fp.seek(0)
	outfp = StringIO.StringIO()
	rsrcmgr = PDFResourceManager()
	device = TextConverter(rsrcmgr, outfp, laparams = LAParams())
	process_pdf(rsrcmgr, device, fp)
	device.close()
	t = outfp.getvalue()
	outfp.close()
	fp.close()
	return t

