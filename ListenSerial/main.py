# -*- coding: utf-8 -*-

#-- based on: https://raw.githubusercontent.com/Jonty/RemoteSensors/master/remoteSensors.py

SERIAL_PORT_NAME = 'COM19'
SERIAL_PORT_SPEED = 115200
import sqlite3
import time
import serial

ser = None
conn = sqlite3.connect('comm.sqlite', check_same_thread=False)
#conn.execute("create table mess (id integer not null primary key AUTOINCREMENT,ans text,ts DATETIME DEFAULT CURRENT_TIMESTAMP);")
#conn.commit()

def main():
	global ser
	ser = serial.Serial(SERIAL_PORT_NAME, SERIAL_PORT_SPEED, timeout=10)
	ser.write('AT+CLIP=1\r\n')
	while 1:
		print(get_full_line_from_serial())
		
	conn.close()


captured = ''
def get_full_line_from_serial():
    
    global captured
    part = ser.readline()
    if part:
        captured += part
        parts = captured.split('\n', 1);
        if len(parts) == 2:
			captured = parts[1]
			if len(parts[0])>1:
				conn.execute("insert into mess (id, ans) values (Null,'"+parts[0]+"');")
				conn.commit()
				return parts[0]
            
    return None
    
    
if __name__ == '__main__':
    main()