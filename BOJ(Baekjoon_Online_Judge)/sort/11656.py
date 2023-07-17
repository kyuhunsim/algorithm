s=input()

def print_sorted_suffixes(string):
    suffixes = []
    for i in range(len(string)):
        suffixes.append(string[i:])
    suffixes.sort()
    for suffix in suffixes:
        print(suffix)

print_sorted_suffixes(s)
