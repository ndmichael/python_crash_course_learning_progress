# strips, rstrips, lstrips
# partition, split
# removeprefix 

fav_language = ' Python '
longer_str = 'Help on method_descriptor in str'
url = 'https://ndmichael.github.io'

print(f'\'{fav_language.lstrip()}\'')
print(f'\'{fav_language.rstrip()}\'')
print(f'\'{fav_language.strip()}\'')

print(f"{longer_str.partition(' ')}")
print(f"{longer_str.split(' ')}")

print(url.removeprefix('https://'))

