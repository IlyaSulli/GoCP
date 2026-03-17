def combine_word_documents(files) :
	combined_document = Document('empty.docx')
	count, number_of_files = 0, len(files)
	for file in files :
		sub_doc = Document(file)
		if count < number_of_files - 1 :
			sub_doc.add_page_break()
		for element in sub_doc._document_part.body._element :
			combined_document._document_part.body._element.append(element)
		count += 1
	combined_document.save('combined_word_documents.docx')


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

