from bs4 import BeautifulSoup
import requests
import csv

headers = {
    "User-Agent": "David_John"
}

page_html = requests.get(
    "https://en.wikipedia.org/wiki/Machine_learning",
    headers=headers
).text

parsed_html_document = BeautifulSoup(page_html, "html.parser")

main_content_div = parsed_html_document.find("div", id="mw-content-text")
tables = main_content_div.find_all("table")

target_table = None

for table in tables:
    rows = table.find_all("tr")
    if len(rows) >= 4:
        target_table = table
        break

# Extract headers
header_cells = target_table.find_all("th")

if header_cells:
    headers = [cell.text.strip() for cell in header_cells]
else:
    first_row = target_table.find_all("tr")[0]
    num_cols = len(first_row.find_all("td"))
    headers = [f"col{i+1}" for i in range(num_cols)]

# Extract data rows
data_rows = []

for row in target_table.find_all("tr")[1:]:
    cells = row.find_all(["td", "th"])
    row_data = [cell.text.strip() for cell in cells]

    while len(row_data) < len(headers):
        row_data.append("")

    data_rows.append(row_data)

# Save to CSV
with open("wiki_table.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(data_rows)

print(headers)
for row in data_rows:
    print(row)
