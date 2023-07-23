import socket, json
import _thread # threadeles
from prog import gyujtAkkord, szita, dalok, kikapcsolLedek, gyujtAkPengetes,gyujtPengFajta, gyujtAkkordFelbont1, gyujtAkkordFelbont3
def szivveresHallgato():
        try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

                s.bind(('0.0.0.0', 9001))
                s.listen(100)
                while True:
                        c, addr = s.accept()
                        data = c.recv(1024).decode()
                        try:
                                data = json.loads(data)
                                print(data)
                                if data['request'] == 'isOnline':
                                        resp = {
                                                'response' : 'OK',
                                                'name': 'raspberry1'
                                        }
                                        c.send(json.dumps(resp).encode())
                                elif data['request'] == 'showChord':
                                        gyujtAkkord(data['chord'])
                                elif data['request'] == 'showSong':
                                        dalok(data['song'])
                                elif data['request'] == 'showAkPeng':
                                        gyujtAkPengetes(data['akpeng'])
                                elif data['request'] == 'showPengFajta':
                                        gyujtPengFajta(data['pengfajta'])
                                elif data['request'] == 'showAkkordFelbont1':
                                        gyujtAkkordFelbont1(data['akkordfelbont1'])
                                elif data['request'] == 'showAkkordFelbont3':
                                        gyujtAkkordFelbont3(data['akkordfelbont3'])
                                elif data['request'] == 'kikapcs':
                                        kikapcsolLedek()
                                elif data['request'] == 'showSong':
                                        dalok(data['song'])
                        except TypeError as TE:
                                print(TE)
        except Exception as e:
                print(e)


szivveresHallgato()
