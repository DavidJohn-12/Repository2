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

# Find main content
main_content_div = parsed_html_document.find("div", id="mw-content-text")

# Find all h2 headings
all_h2_headings = main_content_div.find_all("h2")

# Words to exclude
excluded_words = ["References", "External links", "See also", "Notes"]

clean_headings = []

# Process headings
for heading in all_h2_headings:
    text = heading.text.strip()
    text = text.replace("[edit]", "").strip()

    skip = False
    for word in excluded_words:
        if word in text:
            skip = True
            break

    if not skip:
        clean_headings.append(text)

# Save to file
with open("headings.txt", "w", encoding="utf-8") as file:
    for heading in clean_headings:
        file.write(heading + "\n")
