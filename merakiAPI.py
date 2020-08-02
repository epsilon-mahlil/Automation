import requests
from requests.auth import  HTTPBasicAuth
import base64

URL="http://dev.web.local"
REQUESTS_RETRIES =3
WAIT_FOR_RETRY=1
USERNAME='cisco'
PASSWORD='1234QWer'

def send_request(url,data,headers):
	tries=0
	while True:
		tries+=1
		try :
			response=request(url=url,json=data,headers=headers)
		except :
			pass
def to_base64(s):
	return base64.base64encode(s.encode('utf8')).decode('utf8')
def basic_auth():
	url=URL+'/login'
	#creds=
	#headers=
	#response=
	print(response)
 	#return response.get('')
## Bearer Token
def invoke_info_v2(bearer_token, name):
	url=URL+'/v2/info'
	#data=
	#headers=
	#response=
	print(response)
if __name__ =='__main__':
	print("Basi Auth")
 	#api_key=basic_auth()
	print('----------------')
	#bearer_token=invoke_info_v1(api_key,'')
	print("--------------------")
	print("bearer Token Auth')
	#invoke_info_v2(bearer_token,'')

