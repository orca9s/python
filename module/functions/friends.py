def send_message():
	friend = input('보낼 사람을 쓰세요:')
	message = input('메세지를 써 주세요:')
	print('{}에게 {}메세지를 보냈습니다.'.format(friend,message))

if __name__ == '__main__':
	send_message()
