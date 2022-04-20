# IMPORT ALL THE GOODIES
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from twilio.rest import Client
import twilio 

# WEBPAGE INFORMATION
url = 'https://www.livecoinwatch.com/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage,'html.parser')

cryptocurrecny_table = soup.find('table')
cryptocurrecny_rows = cryptocurrecny_table.findAll('tr')

# TOP FIVE CRYPTOCURRENCIES FORMATTED AND PRINTED
print()
print('Top 5 Cryptocurrency Companies Currently:')

for x in range(1,6):
    td = cryptocurrecny_rows[x].findAll('td')
    rank = td[0].text
    name = td[1].text
    price = float(td[2].text.strip('$'))
    percent_change = float(td[8].text.strip('%'))
    current_price = '${:,.2f}'.format(price)

    print()
    print('Currency Ranking:',rank)
    print('Currency:', name)
    print('Current Price:',current_price)
    print('Percent Change:',percent_change,'%')

    change = round((price)/(1+percent_change/100),2)
    format_change = '${:,.2f}'.format(change)

# TWILIO FOR ALERTS
    AccountSID = 'ACcad0b41f59592a0d10bf35bb47b37d73'
    AuthToken = 'e783538a884b373bae999fdafd7cf216'
    client = Client(AccountSID,AuthToken)
    TwilioNumber = '+18324027045'
    mycellphone = '+18325257900'

# BTC AND ETH ALERTS
    if 'Bitcoin' in name and price < 40000:
        Bitcoin_text = client.messages.create(to = mycellphone, from = TwilioNumber, body ='Bitcoin is below $40,000 currently.')
    if 'Ethereum' in name and price < 3000:
        Ethereum_text = client.messages.create(to = mycellphone, from = TwilioNumber, body ='Ethereum is below $3,000 currently.')
