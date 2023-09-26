source = "sourcefile.txt"
destination = "destination.txt"

with open(source,'r') as source_file:
    content = source_file.read()

with open(destination,'w') as destination_file:
    destination_file.write(content)
