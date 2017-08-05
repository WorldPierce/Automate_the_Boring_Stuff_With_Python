import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

print(res.status_code)
print(len(res.text))
print(res.text[:500])

# badRes requests.get('dfsdfdsafdsa')
# badRes.raise_for_status() # ends program if bad download happens

playFile = open('RomeoAndJuliet.txt', 'wb') # must wb to maintain unicode data
for chunk in res.iter_content(100000): # iterates through res by 100000 bytes
    playFile.write(chunk)

playFile.close()

