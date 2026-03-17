def combine_word_documents(files) :
	merged_document = Document()
	for index, file in enumerate(files) :
		sub_doc = Document(file)
		if index < len(files) - 1 :
			sub_doc.add_page_break()
		for element in sub_doc.element.body :
			merged_document.element.body.append(element)
	merged_document.save('merged.docx')


def combine_word_documents(input_files) :
	for filnr, file in enumerate(input_files) :
		if 'offerte_template' in file :
			file = os.path.join(settings.MEDIA_ROOT, file)
		if filnr == 0 :
			merged_document = Document(file)
			merged_document.add_page_break()
		else :
			sub_doc = Document(file)
			if filnr < len(input_files) - 1 :
				sub_doc.add_page_break()
			for element in sub_doc.element.body :
				merged_document.element.body.append(element)
	return merged_document

