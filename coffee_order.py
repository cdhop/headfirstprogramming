#!/usr/bin/python3

def get_price():
    import urllib.request
    page = urllib.request.urlopen("http://www.beans-r-us.appspot.com/prices-loyalty.html")
    text = page.read().decode("utf8")

    where = text.find('>$')
    start_of_price = where + 2
    end_of_price = start_of_price + 4

    return(float(text[start_of_price:end_of_price]))

price_now = input("Do you want to see the price now (Y/N)? ")
if price_now.upper() == 'Y':
    print(get_price())
else:
    price = 99.99
    while price > 4.74:
        price = get_price()
    print('Buy! ' + str(price))

