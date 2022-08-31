from Wappalyzer import Wappalyzer, WebPage

def build_with(url):
    webpage = WebPage.new_from_url(url)
    wappalyzer = Wappalyzer.latest()
    return wappalyzer.analyze_with_versions_and_categories(webpage)