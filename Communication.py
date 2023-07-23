import socket, json

def keresFutoSzerver():
	szerverek = []
	for i in range(100, 110):
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.settimeout(.01)
			s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			s.connect(('192.168.0.%d' % i, 9001))
			s.send(json.dumps({
				'request': 'isOnline'
			}).encode())
			response = json.loads(s.recv(1024).decode())
			if response['response'] == 'OK':
				szerverek.append({
					'name' : response['name'],
					'ip': '192.168.0.%d' % i
				})
			s.close()
		except socket.timeout as e:
			pass
	return szerverek

def kuldAkkord(ip, chord):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.connect((ip, 9001))

		s.send(json.dumps({
			'request': 'showChord',
			'chord': chord
		}).encode())

		s.close()

	except Exception as e:
			print(e)

def kuldDal(ip, song):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.connect((ip, 9001))

		s.send(json.dumps({
			'request': 'showSong',
			'song': song
		}).encode())

		s.close()

	except Exception as e:
			print(e)

def kuldDalAkkord(ip, chord):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.connect((ip, 9001))

		s.send(json.dumps({
			'request': 'showDalAkkord',
			'chord': chord
		}).encode())

		s.close()

	except Exception as e:
			print(e)

def kuldAkkordPengetes(ip, akpeng):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.connect((ip, 9001))

		s.send(json.dumps({
			'request': 'showAkPeng',
			'akpeng': akpeng
		}).encode())

		s.close()

	except Exception as e:
			print(e)

def kuldPengetesFajtak(ip, pengfajta):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.connect((ip, 9001))

		s.send(json.dumps({
			'request': 'showPengFajta',
			'pengfajta': pengfajta
		}).encode())

		s.close()

	except Exception as e:
			print(e)

def kuldAkkordFelbont1(ip,akkordfelbont1):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.connect((ip, 9001))

		s.send(json.dumps({
			'request': 'showAkkordFelbont1',
			'akkordfelbont1': akkordfelbont1
		}).encode())

		s.close()

	except Exception as e:
			print(e)

def kuldAkkordFelbont2(ip,akkordfelbont2):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.connect((ip, 9001))

		s.send(json.dumps({
			'request': 'showAkkordFelbont2',
			'akkordfelbont2': akkordfelbont2
		}).encode())

		s.close()

	except Exception as e:
			print(e)

def kuldAkkordFelbont3(ip,akkordfelbont3):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.connect((ip, 9001))

		s.send(json.dumps({
			'request': 'showAkkordFelbont3',
			'akkordfelbont3': akkordfelbont3
		}).encode())

		s.close()

	except Exception as e:
			print(e)

def kuldKikapcs(ip):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		s.connect((ip, 9001))

		s.send(json.dumps({
			'request': 'kikapcs'

		}).encode())

		s.close()

	except Exception as e:
			print(e)

if __name__ == '__main__':
	t = keresFutoSzerver()
	print(t)