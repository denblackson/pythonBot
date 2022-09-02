import datetime
import json
import requests
from googletrans import Translator

answer = requests.get('https://yesno.wtf/api')
print(answer)
yes_or_not = json.loads(answer.text)
print(yes_or_not)