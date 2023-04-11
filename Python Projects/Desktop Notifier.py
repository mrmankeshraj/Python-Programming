from plyer import notification
import time

if __name__ == '__main__':
	while True:
	    notification.notify(
		    title="***** Take Rest *****",
		    message="It will Give you an Energy Surge and also helps you in your Mental Health.",
		    app_icon="B:/Python Programming/Python Projects/Mental Health",
		    timeout=5)
	    time.sleep(10)