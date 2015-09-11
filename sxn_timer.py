import threading
import time

def print_tid(param):
	print('default print: tid({})'.format(param.pop()))

class Sxn_timer(threading.Thread):
	"""docstring for Sxn_timer"""
	def __init__(self, seconds, action=print_tid, action_param=[]):
		super(Sxn_timer, self).__init__()
		self.runTime = seconds
		self.action = action
		self.action_param = action_param
		pass

	def run(self):
		time.sleep(self.runTime)
		t = Sxn_timer(self.runTime, self.action, self.action_param)
		t.start()
		if [] == self.action_param:
			self.action_param.append(self.ident)
		self.action(self.action_param)


	
def print_something(param):
	for x in param:
		print(x)
	pass


if __name__ == '__main__':

	out_put = ['a', 1, 'songxiaoning']

	t = Sxn_timer(2, print_something, out_put)
	t.start()
	
	pass
