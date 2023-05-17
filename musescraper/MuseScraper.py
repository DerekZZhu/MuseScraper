import requests as r
import urllib.request
from requests_html import HTMLSession
import time

class MuseScraper():
    def __init__(self):
        self.auth_token = "38fb9efaae51b0c83b5bb5791a698b48292129e7"


    def fetchApiUrl(self, _id, _type="pdf", file_name="", file_path=""):
        response = r.get(f'https://musescore.com/api/jmuse?id={_id}&index=0&type={_type}&v2=1',
                        headers = {"authorization": self.auth_token})
        url = response.json()['info']['url']
        urllib.request.urlretrieve(url, f"{file_path}{file_name}")


    def massScrapeIds(search_term="", level="", num=5, page_num=1, sort="") -> list:
        scores = []
        session = HTMLSession()
        page = session.get(f"https://musescore.com/sheetmusic?text={search_term}&complexity={level}&page={page_num}&sort={sort}")
        page.html.render(sleep=20, timeout=100)

        for link in page.html.absolute_links:
            if "scores" in link and len(scores) < num:
                # print(link)
                scores.append(link.split("/")[-1])

        return scores


    def massScrape(self, pages=5, level=1, sort="", search_term=""):
        for i in range(1, pages):
            print(f"Batch{i}")
            scores = self.massScrapeIds(num=20, page_num=i, level=level, sort=sort, search=search_term)
            for j in scores:
                self.fetchApiUrl(j, "midi", self.auth_token, f"{j}.midi")
                time.sleep(30)
