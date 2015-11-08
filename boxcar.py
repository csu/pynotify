import requests

import boxcar_secrets
from notify import Notifier

class BoxcarNotifier(Notifier):
    def send(self, message, recipient=None, title=None, source=None, open_url=None):
        params = {
            'user_credentials': boxcar_secrets.RECIPIENT_ACCESS_TOKEN
        }

        params['notification[long_message]'] = message

        if title:
            params['notification[title]'] = title
        if source:
            params['notification[source_name]'] = source
        if open_url:
            params['notification[open_url]'] = open_url

        requests.post("https://new.boxcar.io/api/notifications", params=params)

    def quick_send(self, message):
        self.send(message, title=message, source='modapi')

if __name__ == '__main__':
    boxcar = BoxcarNotifier()
    boxcar.send('test', title='hi', source='modapi')