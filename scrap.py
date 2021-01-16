import requests, json, base64
time = int(input('How much codes You want?\n'))
url = 'https://www.hackthebox.eu/api/invite/generate'
codes = []
user_agent = {'User-agent': 'Mozilla/5.0'}

for i in range(1, time):
	r = requests.post(url, headers=user_agent)
	r = r.json()
	data = r['data']
	enc_data = data['code']
	code = base64.b64decode(enc_data).decode('utf-8')
	codes.append(code)

for code in codes:
	print(code)
