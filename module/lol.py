from functions.game import*
from functions.shop import show_info as shop_info
from functions import shop
from functions import friends

def turn_on():
	print('= Turn on game=')

	while True:
		choice=input('뭐할래\n 1: 상점가기\n 2:게임시작하기\n 3:메세지\n4:종료\n 입력.')
		if choice == '1':
			shop.buy_item()
		elif choice == '2':
			game.play_game()
		elif choice == '3':
			friends.send_message()
		elif choice == '4':
			break
		else:
			print('1, 2, 3, 4중 하나를 입력하세요')

if __name__ == '__main__':
	turn_on()
