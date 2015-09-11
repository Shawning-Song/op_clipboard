# op_clipboard

import pyperclip
import os
import sys
import threading
import Sxn_timer


file_server = r'xx'
my_direct = file_server + r'\xx'
my_file_path = my_direct + r'\clipboard_file.txt'
flag_file_path = my_direct + r'\flag_file'

def get_clip_text():
	return pyperclip.paste()
	pass

def set_clip_text(text):
	pyperclip.copy(text)
	pass

def save_clipboard_text(param=[]):
	if False == os.path.exists(my_direct):
		os.mkdir(my_direct)
	
	clipboard_file = open(my_file_path, 'w+')
	clipboard_data = get_clip_text()

	try:
		clipboard_file.write(clipboard_data)	
	except (UnicodeEncodeError):
		print('encode error.')

	print('save clipboard text into clipboard_file.txt')
	clipboard_file.close()
	pass

def change_clipboard_text(param=[]):
	if False == os.path.exists(my_direct):
		os.mkdir(my_direct)

	clipboard_file = open(my_file_path, 'r')
	file_data = clipboard_file.read()

	set_clip_text(file_data)

	print("set clipboard_file.txt's data info clipboard.")
	clipboard_file.close()
	pass
 
 def do_copy_set(param=[])
 	save_clipboard_text()
 	change_clipboard_text()
 	pass

if __name__ == "__main__":
	t = Sxn_timer.Sxn_timer(1,do_copy_set)
	t.start()
	pass
