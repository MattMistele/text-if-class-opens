import argparse
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

def main():

	proxy_client = TwilioHttpClient()
	proxy_client.session.proxies = {'https': os.environ['https_proxy']}

	# TWILIO SETUP STUFF
	# Your Account SID from twilio.com/console
	account_sid = "YOUR_ACCOUNT_SID"
	# Your Auth Token from twilio.com/console
	auth_token  = "YOUR_AUTH_TOKEN"
	client = Client(account_sid, auth_token)

	BASE_URL = 'https://www.scu.edu/apps/ws/courseavail/search/4000/ugrad/math+51'
	print("url: " + BASE_URL)


	#get the json response from a URL
	r = requests.get(BASE_URL)
	json_file = r.json() # if response type was set to JSON, then you'll automatically have a JSON response here...

	results = json_file['results']

	print

	for i in results:
		#define all useful vars
		name = i['subject'] + " " + i['catalog_nbr'] + ": " + i['class_descr']
		number = i['class_nbr']
		time = i['mtg_days_1'] + " " + i['mtg_time_beg_1']
		prof = i['instr_1']
		seats = int(i['seats_remaining'])

		#print out the results
		print(name)
		print(number)
		print(time)
		print(prof)
		print("Seats: " + str(seats))


		# MYSTUFF
		if(number == "74942"):
			if(seats > 0):
				message = client.messages.create(to="+YOUR_NUMBER_HERE", from_="+12065391594", body=("Your class has " + seats + " left!"))
				print("Your class has " + str(seats) + " seats left!")

		print

if __name__ == '__main__':
	main()