import string

infile=open('sample-file.txt','r')
lines=infile.readlines()
infile.close()

normalized_lines={}

line_number = 1

for line in lines:
    original_line = line.rstrip()   # remove newline at the end
    cleaned = ""

    for char in original_line:
        char = char.lower()
        if char.isalnum():
            cleaned += char

    if cleaned == "": #SKIP EMPTY LINES
        line_number += 1
        continue

    # store the result
    if cleaned in normalized_lines:
        normalized_lines[cleaned].append((line_number, original_line))
    else:
        normalized_lines[cleaned] = [(line_number, original_line)]

    line_number += 1


duplicate_sets = [] #list for duplicates

for key in normalized_lines:
    if len(normalized_lines[key]) > 1:
        duplicate_sets.append(normalized_lines[key])

print(duplicate_sets)

print("Number of near-duplicate sets:", len(duplicate_sets)) #prints number of duplicate sets

print("\nFirst two near-duplicate sets:")

count = 0

for sett in duplicate_sets:
    if count == 2: #number of sets is 2 then stop
        break

    print("\nSet", count + 1)
    for line_info in sett:
        line_num = line_info[0] #gets the number
        text = line_info[1] #gets the text
        print(f"Line {line_num}: {text}")

    count += 1
