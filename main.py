import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, "src")
sys.path.insert(0, src_dir)

from scraper import SimpleWebScraper


def main():
    target_url = "https://automatetheboringstuff.com/2e/"
    scraper = SimpleWebScraper(target_url)

    scraped_data = scraper.scrape_main_titles()

    if scraped_data:
        print("\n--- Scraped Data ---")
        print(f"Book Title: {scraped_data['book_title']}")
        print("\nChapter Titles:")

        if scraped_data["chapter_titles"]:
            for i, title in enumerate(
                scraped_data["chapter_titles"], start=1
            ):
                print(f"{i}. {title}")
        else:
            print("No chapter titles found.")

        print("--------------------")
    else:
        print("Failed to scrape data.")


if __name__ == "__main__":
    main()
