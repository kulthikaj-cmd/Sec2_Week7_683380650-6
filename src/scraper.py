import requests
from bs4 import BeautifulSoup

class SimpleWebScraper:
    def __init__(self, target_url):
        self.target_url = target_url

    def _get_html_content(self):
        try:
            response = requests.get(
                self.target_url,
                headers={"User-Agent": "Mozilla/5.0"},
                timeout=10
            )
            response.raise_for_status()
            print("Successfully downloaded content.")
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}")
            return None

    def scrape_main_titles(self):
        html = self._get_html_content()
        if not html:
            return None

        soup = BeautifulSoup(html, "html.parser")
        book_title = soup.title.get_text(strip=True) if soup.title else "Book Title Not Found"

        chapter_titles = []
        for tag in soup.find_all(["h1", "h2", "h3"]):
            title = tag.get_text(" ", strip=True)
            if title and title not in chapter_titles:
                chapter_titles.append(title)

        return {
            "book_title": book_title,
            "chapter_titles": chapter_titles
        }
