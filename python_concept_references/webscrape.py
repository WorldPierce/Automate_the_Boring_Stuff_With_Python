import bs4, requests
#beautifulsoup4 ^^

res = requests.get('https://www.amazon.com/gp/product/1593275994/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1593275994&linkCode=as2&tag=playwithpyth-20&linkId=HDM7V3T6RHC5VVN4')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser') # hhtml.parser hides warning

# inspect element and Copy Selector in chrome
elems = soup.select('#mediaNoAccordion > div.a-row > div.a-column.a-span4.a-text-right.a-span-last > span.a-size-medium.a-color-price.header-price')
#elems is list object

print(elems[0].text.strip())
