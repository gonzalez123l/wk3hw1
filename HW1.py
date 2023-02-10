with open ("files/regex_test.txt") as f:
    data = f.readlines()
    print (data)
    
pattern = re.compile("([A-Z][a-z]+), ([\w -]*)([A-Z][a-z]+), ([A-Z][a-z]+$)")

for person in data:
    match = pattern.search(name)
    
    if match:
        print('\n', f"{match.group(1)} {match.group(2)}{match.group(3)}")