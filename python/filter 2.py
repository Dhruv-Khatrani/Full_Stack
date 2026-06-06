strings = ["hello","","world","","python"]

non_empty_strings = filter(lambda x: x!="",strings)

print(list(non_empty_strings))
