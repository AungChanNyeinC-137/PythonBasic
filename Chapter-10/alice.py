file_name = 'alice.txt'
try: 
    with open(file_name) as file_obj:
        contents = file_obj.read()
except FileNotFoundError:
    print(f"{file_name} was not found")
else:
    words = contents.split()
    num_words = len(words)
    print(f"the file '{file_name}' has about {num_words} words")
    