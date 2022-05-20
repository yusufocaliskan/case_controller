# Details

Hi, I wrote a Python crawler...

Developers in Turkey, especially those who stand with socialism, are not only dealing with problems related to code but also, before everything, we have a common problem like freedom which is caused by the government's policy...

Occasionally it could take time to control and observe the whole permitted cases one by one. This small python that I named "Ugly Boy" will help you to take off the load.

The script simply goes to "Uyap" website, logging with the information, and then sends you an e-mail.

## Installation
The only thing that you should do, downloads the requirements.

`` pip install -r requirements.txt ``

Set the .env file

``USER_NAME = 'your-tr-no:'``

``USER_PASSWORD = 'e-devlet password'``

``MAIL_FROM = 'an-email'``

``MAIL_TO = 'an-email'``

``MAILGUN_KEY = 'mail-ru-api-key'``


save it as .env

Than run the uyap.py
`` python3 uyap.py ``

The result will be sent you to in the mail that sets MAIL_TO