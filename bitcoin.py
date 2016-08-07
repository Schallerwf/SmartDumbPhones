import requests

def bitcoinPrice():
	 response = requests.get('https://chain.so/api/v2/get_price/BTC/USD',verify=True)
	 info = response.json()

	 priceUSD = info['data']['prices'][1]['price']
	 return '1 BTC = ' + priceUSD + ' USD'