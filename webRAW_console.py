from pywnp import WNPRedux
import pypresence
import time 
import psutil
from psutil._common import bytes2human
import wmi
computer = wmi.WMI()

choose = int(input("1 - GawrGura\n2 - Ayaka\n3 - Hu Tao\n4 - Vampire\n\nChoose: ")) 

arr = {
   'title': '',
   'artist': '',
   'platform': ''
}

RPC = pypresence.Presence(client_id='939445325570125894')

RPC.connect()

def logger(type, message):
  print(f'{type}: {message}')

WNPRedux.start(1234, '1.0.0', logger)

i = 1

def RPCUpdate(state, details, pltform):
        global i

        current_date = time.localtime()
        start_of_day = time.struct_time((current_date.tm_year, current_date.tm_mon, current_date.tm_mday, 0, 0, 0, current_date.tm_wday, current_date.tm_yday, current_date.tm_isdst))
        start_of_day_unix = time.mktime(start_of_day) 

        large_image = ""
        large_text = ""

        if int(choose) == 1:
            large_image = "gawrgura_large"
            large_text = "Акуляля"
        elif int(choose) == 2:
            large_image = "ayaka"
            large_text = "Аяка"
        elif int(choose) == 3:
            large_image = "hu_tao_large"
            large_text = "Хутава"
        elif int(choose) == 4:
            large_image = "vamp"
            large_text = "Кровосися"

        print(start_of_day_unix)

        small_image = ''
        small_text = ''

        if pltform == "YouTube Music":
            small_image = 'ytm'
            small_text = 'YouTube Music'
        elif pltform == "YouTube":
            small_image = 'yt'
            small_text = 'YouTube'
        else: 
            small_image = 'hu_tao_large'
            small_text = 'Хутава'

        if state == "" and pltform == "Base":
            
            if i == 1:
                memory = psutil.virtual_memory()

                state = f"{computer.Win32_VideoController()[0].Name} | RAM: {bytes2human(memory.used)}/{bytes2human(memory.total)}" 
                details = f"{computer.Win32_Processor()[0].Name}" 

                i = 0
            else:
                
                state = "I'm a cute shark!"
                details = "I Love You!"

                i = 1

        RPC.update(
            state=state,
            details=details,
            large_image=large_image, 
            large_text=large_text, 
            small_image=small_image,  
            small_text=small_text,
            start=int(start_of_day_unix)
        )

def GetInfo():
  time.sleep(10)
  if WNPRedux.is_started and isinstance(WNPRedux.media_info.artist, str) and WNPRedux.media_info.state == 'PLAYING':
     arr['artist'] = WNPRedux.media_info.artist
     arr['title'] = f"{WNPRedux.media_info.title} {WNPRedux.media_info.position}/{WNPRedux.media_info.duration} ({round(WNPRedux.media_info.position_percent, 1)}%)"
     arr['platform'] = WNPRedux.media_info.player_name

     RPCUpdate(arr["artist"], arr["title"], arr['platform'])
  else:
     RPCUpdate("", "", 'Base')

def Start():
    try:
        while True:
            GetInfo() 
    except KeyboardInterrupt:
        pass
    finally:
        # RPC.close()
        pass