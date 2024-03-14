def extractTextFrom(webContent, printedtexts):
    divs = webContent.find_all(["div"])
    for div in divs:
        headers = div.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        divheader = ""
        for header in headers:
            divheader = header.text.strip() + " "
        
        texts = div.find_all(['p'])
        divtext = ""
        for text in texts:
            divtext = text.text.strip() + " "
            
        spans = div.find_all(['span'])
        spantext = ""
        for span in spans:
            spantext=span.text.strip() + " "

        fulltext = "Title: "+ divheader + "Text: " + divtext + "Span text: " + spantext
        print(fulltext)