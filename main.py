import json

def main():
	print('Type help for commands')
	print('\n')
	with open('data.json', 'r') as f:
		dataJson = json.load(f)
	
		data = {
			'Campaigns': dataJson['Campaigns'],
			'Experiences': dataJson['Experiences'],
			'Messages': [Message for Message in dataJson['Messages']],
			'Purchases': dataJson['Purchases'],
			'RoomsAndInteractions': dataJson['RoomsAndInteractions'],
			'Spotify': dataJson['Spotify'],
			'SwipeNotes': dataJson['SwipeNotes'],
			'SwipeParty': dataJson['SwipeParty'],
			'Usage': dataJson['Usage'],
			'User': dataJson['User'],
			'Photos': dataJson['Photos']
		}
	
		campaigns = {
			'current_campaigns': data['Campaigns']['current_campaigns'],
			'expired_campaigns': data['Campaigns']['expired_campaigns']
		}
	
		messages = {
			'messages': [message['messages'] for message in data['Messages'] if len(message['messages']) != 0]
		}
	
		purchases = {
			'subscription': data['Purchases']['subscription'],
			'consumable': data['Purchases']['consumable'],
			'boost_tracking': data['Purchases']['boost_tracking'],
			'super_like_tracking': data['Purchases']['super_like_tracking']
		}
	
		roomAndInteractions = {
			'rooms': data['RoomsAndInteractions']['rooms']
		}
	
		spotify = {
			'spotify_connected': data['Spotify']['spotify_connected'],
			'spotify_username': data['Spotify']['spotify_username'],
			'spotify_user_type': data['Spotify']['spotify_user_type'],
			'spotify_last_updated_at': data['Spotify']['spotify_last_updated_at'],
			'spotify_theme_track': {'Name': data['Spotify']['spotify_theme_track']['name'],
									'Album': data['Spotify']['spotify_theme_track']['album']['name'],
									'Artists': data['Spotify']['spotify_theme_track']['artists'][0]['name']},
			'spotify_top_artists': [{'Name': song['top_track']['name'], 'Album': song['top_track']['album']['name'], 'Artists': song['name']} for song in data['Spotify']['spotify_top_artists']]
		}
	
		useage = {
			'app_opens': sum([data['Usage']['app_opens'][item] for item in data['Usage']['app_opens']]),
			'swipes_likes': sum([data['Usage']['swipes_likes'][item] for item in data['Usage']['swipes_likes']]),
			'swipes_passes': sum([data['Usage']['swipes_passes'][item] for item in data['Usage']['swipes_passes']]),
			'swipes_total' : sum([data['Usage']['swipes_likes'][item] for item in data['Usage']['swipes_likes']]) + sum([data['Usage']['swipes_passes'][item] for item in data['Usage']['swipes_passes']]),
			'superlikes': sum([data['Usage']['superlikes'][item] for item in data['Usage']['superlikes']]),
			'matches': sum([data['Usage']['matches'][item] for item in data['Usage']['matches']]),
			'messages_sent': sum([data['Usage']['messages_sent'][item] for item in data['Usage']['messages_sent']]),
			'messages_received': sum([data['Usage']['messages_received'][item] for item in data['Usage']['messages_received']]),
			'messages_total': sum([data['Usage']['messages_sent'][item] for item in data['Usage']['messages_sent']]) + sum([data['Usage']['messages_received'][item] for item in data['Usage']['messages_received']]),
			'advertising_id': data['Usage']['advertising_id'],
			'idfa': data['Usage']['idfa']
		}
	
	while True:
		userinput = input('Enter: ')
		print('\n')
		if userinput == 'help':
			print('useage : lists [app_opens, swipes_likes, swipes_passes, total_swipes,\n\t\tsuperlikes, matches, messages_sent, advertising_id, idfa]')
			print('spotify: connected spotify info')
			print('messages: print all mnessages')
			print('campaigns: campaign information')
			print('purchases : purchase information')
			print('roomAndInteractions: roomAndInteractions information')
			print('all : prints all data')
			print('\n')

		elif userinput == 'all':
			print(data)
			print('\n')
		elif userinput == 'messages':
			print(messages)
			print('\n')
		elif userinput == 'useage':
			print(useage)
			print('\n')
		elif userinput == 'spotify':
			print(spotify)
			print('\n')
		elif userinput == 'campaigns':
			print(campaigns)
			print('\n')
		elif userinput == 'purchases':
			print(purchases)
			print('\n')
		elif userinput == 'roomAndInteractions':
			print(roomAndInteractions)
			print('\n')

if __name__ == '__main__':
	print('\n')
	print('If you haven\'t downloaded your Tinder data\nIt can be requested at the link below\nhttps://account.gotinder.com/login?from=%2Fdata')
	print('\n')
	print('Once you have your data extract it from Tinder.zip')
	print('Place data.json in the same directory as main.py')
	print('\n')
	main()