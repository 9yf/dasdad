import requests
import time
while True:
	url = 'https://discord.com/api/v8/channels/1024836060934590536/messages'
	data = {"content": "J4J DM now no bots"}
	header = {"authorization": "MTAwMDUwNjA0MzkyMDU1MjAxNw.GwA5Ij.x9hDYCALpIsh6SdQezqCYYxjmvXKdltvE9Viz4"}
	r = requests.post(url, data=data, headers=header)
	print(r.status_code)
	time.sleep(31)