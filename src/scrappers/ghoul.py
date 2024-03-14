from src.utils.url_utils import checkUrl, responseUrl
from src.scrappers.text_extractor import extractTextFrom

def ghoulAction():
    url = ''
    urlVerified = checkUrl(url)
    if urlVerified == True:
        webContent = responseUrl(url)
        extractTextFrom(webContent)
        #ExtractImages
        #ExtractLinks
        #ExtractVideos
        #ExtractAudio
        #ExtractEmbeds
        #ExtractForms
        #ExtractTables
        #ExtractScripts
        #ExtractFrames
        #ExtractIframes
        #ExtractObjects
        #ExtractAnchors
        #ExtractMeta
        #OrderOnExcelOrSomething
        #Save
    else:
        print("")