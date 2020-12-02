import time
import vk_api

secret_key = 'my secret key'
service_token = 'my long service tokennnnnnnnnnnnnnnnnnnnnnnnnnnnn'
my_app_id = '1234567'
my_login = 'nouser@mailinator.com'
my_password = 'qwerty123'

# Uncomment line below to change working directory to correct one 
#os.chdir('/home/pushkin/vk/online')

vk_session = vk_api.VkApi(login=my_login, password=my_password, app_id=my_app_id, token=service_token)
vk_session.auth()
api = vk_session.get_api()

while True:
    api.account.setOnline()
    time.sleep(120)