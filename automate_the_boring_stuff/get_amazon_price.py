import bs4, requests

def getAmazonPrice(amazonUrl):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
    res = requests.get(amazonUrl, headers=headers)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")
    elems = soup.select('#price_inside_buybox')
    return elems[0].text.strip()

price = getAmazonPrice('https://www.amazon.com.mx/Twelve-South-Soporte-monitor-abrazadera/dp/B071RWKNF2')
print('The price of the product is: ' + price)
