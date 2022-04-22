NLP Pipeline (generalised)

Data acquisition
Text cleaning
Pre-processing
Feature engineering
Modeling
Evaluation
Deployment
Monitoring and model updating

---

Data acquisition

Use a public dataset
Scrape data
Product intervention
Data augmentation (take a small dataset and use some tricks to create more data. These tricks are also called data augmentation)
	Synonym replacement
	BAck tranlsation
	TF-IDF–based word replacement
	Bigram flipping
	Replacing entities
	Adding noise to data
Active learning


--- 

Text Extraction and Cleanup

	HTML Parsing and Cleanup (exttracting text using Beautiful Soup and Scrapy and removing tags etc)
	Unicode Normalization (symbols, emojis, and other graphic characters)
	Spelling Correction
	System-Specific Error Correction ( when involved with PDF docs or scanned docs)
		for scanned docs use optical character recognition . example tool -  Tesseract


---

Pre-Processing [follow this order]

	Sentence segmentation and word tokenization.
	Stop word removal, lowercasing, removing digits/punctuation
	stemming and lemmatization
	Normalization, language detection, code mixing, transliteration
	POS tagging, parsing, coreference resolution


---

Feature Engineering

	LSI
	TF-IDF
	Cosine similarity


