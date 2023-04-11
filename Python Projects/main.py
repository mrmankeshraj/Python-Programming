from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MainApp(object):
 	"""docstring for ClassName"""
 	def build(self):
 		return MDLabel(text="Welcome to my Application", halign="center")
if __name__ == '__main__':
	MainApp().run()
 		 