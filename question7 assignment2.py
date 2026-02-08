from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "David_John"
}

page_html = requests.get(
    "https://en.wikipedia.org/wiki/Data_science",
    headers=headers
).text

parsed_html_document = BeautifulSoup(page_html, "html.parser")

# Get title safely
page_title = parsed_html_document.find("title")
if page_title is not None:
    print("Page title:", page_title.text)

# Find main content
main_content_div = parsed_html_document.find("div", id="mw-content-text")
if main_content_div is None:
    print("Main content not found")


# Find paragraphs
all_paragraph_elements = main_content_div.find_all("p")

# First paragraph with at least 50 characters
for paragraph in all_paragraph_elements:
    text = paragraph.text.strip()
    if len(text) >= 50:
        print("\nFirst paragraph (≥50 characters):")
        print(text)
        break
