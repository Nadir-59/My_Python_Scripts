
import requests,sys,os,xml,time
from bs4 import BeautifulSoup
class c:
   gw = "\033[90m"
   r = "\033[91m"
   g = "\033[92m"
   y = "\033[93m"
   pp = "\033[94m"
   pk = "\033[95m"
   c = "\033[96m"
   e = "\033[0m"
   white = "\033[97m"
   def __init__(self):
      self.swi = f"{c.e}-{c.y}>{c.e} "
   def __call__(self):
      os.system("clear")
      self.ascci()
      self.menu()
   def animcolor(self,txt):
       new = []
       for i in txt:
          if i =="<":
            new.append(f"{c.y}")
            new.append(i)
          elif i ==">":
            new.append(i)
            new.append(f"{c.e}")
          else:
            new.append(i)
       new.append(f"{c.e}")
       return "".join(new)   
   def anim(self,text,speed=0.020):
      for i in text:
        print(i,end="")
        sys.stdout.flush()
        time.sleep(speed)

   def ascci(self):
     print(f"""  {c.y}_ __ ___{c.e}  _   _   ___  ___ _ __ __ _ _ __  
 | '_ ` _ \| | | | / __|/ __| '__/ _` | '_ \ 
 | | | | | | |_| | \__ \ (__| {c.r}| | (_|{c.e} | |_) |
 {c.y}|_| |_| |_|\__, | {c.r}|___/\___|_|{c.e}  \__,_| .__/ 
             __/ |                    | |    
            |___/                     |_|    
""")

   def menu(self):
      print(f"""{c.r}[1]{c.e}-{c.y}Get html Parser{c.e}        {c.r}[4]{c.e}-{c.y}Settings{c.e}
{c.r}[2]{c.e}-{c.y}get json url{c.e}           {c.r}[5]{c.e}-{c.y}exit{c.e}
""")
      self.switching()
   def savefile(self,soup):
     with open(f"{self.nameUrl}.html","w") as f:
       f.write(str(soup))
     self.anim(f"{c.gw}Time Request{c.e} {self.swi}{self.timeRequest}s")
     print()
     self.anim(f"{c.gw}name file {c.e} {self.swi}{self.nameUrl}.html")
     print()     
     self.anim(f"{c.gw}path{c.e} {self.swi}{c.y}{os.getcwd()}/{self.nameUrl}.html{c.e}")
     print()
     self.anim(f"{c.gw}operation{c.e} {self.swi}{c.g}Sucessfully ! {c.e}")

   def switching(self):
     userput = input(self.swi)
     if userput =="1":
        self.parsing_html()
     elif userput=="5":
        os.system("clear")
        sys.exit()
     else:
        self() 
   def parsing_html(self):
     os.system("clear")
     self.ascci()
     url = input(f"url {self.swi}")
     self.nameUrl = url.split("/")[-1]
     #try request to fetch the url
     try:
        start = time.perf_counter()
        result = requests.get(url)
        end = time.perf_counter()
        t = str(end-start).split(".")
        t[1] = t[1][:2]
        self.timeRequest = ".".join(t)
     except ValueError:
        self.anim(f"{c.y} Url does'nt Exist!{c.e}")
        input()
        self()
     except:
        self.anim(f"{c.r}Make sur you are connect to Internet !?	 !{c.e}")
        input()
        self()
        #save page content/markup
     src = result.content	
     #print(src)
     #create object to parse content
     soup = BeautifulSoup(src,"lxml")
     self.anim(f"{c.gw}Scrapping{c.e} {self.swi}{c.g}Succesfully !{c.e}")
     print()
     self.savefile(soup)
     input()
     return self()
if __name__ == "__main__":
  run = c()
  run()
