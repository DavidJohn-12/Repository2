def find_lines_containing(filename, keyword):
    results = []
    line_number = 1   # start counting lines at 1

    file = open(filename, "r", encoding="utf-8")

    for line in file:
        if keyword.lower() in line.lower():
            results.append((line_number, line.strip()))
        line_number = line_number + 1

    file.close()
    return results

# Test the function
matches = find_lines_containing("sample-file.txt", "lorem")

# Print number of matches
print("Number of matching lines:", len(matches))

# Print first 3 matches
print("\nFirst 3 matching lines:")
for line_number, text in matches[:3]:
    print(f"{line_number}: {text}")