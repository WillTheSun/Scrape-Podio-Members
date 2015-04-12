from pypodio2 import api
import getpass
client_id = "wills-api-scripts"
client_secret = "d7VDyXQetV0sFL4ou2AWXnQ2lfYAjKTphumSnol6yeiODGX0zaazNrrj49dRNFY5"
username = getpass.getpass("Podio username (yale email):")
password = getpass.getpass("Password for %s: " % username)
app_key = 9358522
app_token = "b63305166b8f4c74aa7b17639fc3df6a"



usr=api.OAuthClient(
	client_id,
	client_secret,
	username,
	password
)
b=0

event_absences = usr.Item.filter(app_key, {})

import csv
with open('output.csv', 'w') as csvfile:
	attendees = csv.writer(csvfile)
	attendees.writerow(["Meeting Type"] + ['Member_ID'] + ['Absence Type'])
	#For every event
	for e in event_absences["items"]:
		if str(e['title']) == 'Other':
			print 'Other'
		else:	
			#print e['fields'][1]['values'][0]['start_date'] + " : " + e['title']
			if len(e["fields"]) > 2:
				for i in range (2, len(e["fields"])):
					fieldtype = str(e['fields'][i]['external_id'])
					#print fieldtype + " absence type"
					if fieldtype =='excused-absences-2' or fieldtype =='absences' or fieldtype == '5-or-more-minutes-late':
						for j in e["fields"][i]['values']:
							meeting_type = str(e['fields'][1]['values'][0]['start_date']) + ":" + str(e['title'])
							member = str(j['value']['app_item_id'])
							absence_type = fieldtype
							attendees.writerow([meeting_type] + [member] + [absence_type])



