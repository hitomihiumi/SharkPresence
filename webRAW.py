from pywnp import WNPRedux
import pypresence
import time 
import psutil
from psutil._common import bytes2human
import wmi
from tkinter import *
from PIL import Image, ImageTk
computer = wmi.WMI()



# choose = int(input("1 - GawrGura\n2 - Ayaka\n3 - Hu Tao\n4 - Vampire\n\nChoose: ")) 

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

# time.sleep(10)

i = 1

def RPCUpdate(state, details, pltform):
        global i

        current_date = time.localtime()
        start_of_day = time.struct_time((current_date.tm_year, current_date.tm_mon, current_date.tm_mday, 0, 0, 0, current_date.tm_wday, current_date.tm_yday, current_date.tm_isdst))
        start_of_day_unix = time.mktime(start_of_day) 

        large_image = ""
        large_text = ""

        if int(choose_var.get()) == 1:
            large_image = "gawrgura_large"
            large_text = "Акуляля"
        elif int(choose_var.get()) == 2:
            large_image = "ayaka"
            large_text = "Аяка"
        elif int(choose_var.get()) == 3:
            large_image = "hu_tao_large"
            large_text = "Хутава"
        elif int(choose_var.get()) == 4:
            large_image = "vamp"
            large_text = "Кровосися"

        print(start_of_day_unix)
        # print(large_image, large_text)

        small_image = ''
        small_text = ''
        # state = "safemode"
        # details = "I'm Watching You"

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
                
                state = state_entry.get()
                details = details_entry.get()

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

def select_choose():
    global choose
    choose = int(choose_var.get())

# Создание главного окна Tkinter
root = Tk()
root.title("PyRPC Control")
root.geometry("400x400")

bg_image = Image.open("bg.png")
bg_photo = ImageTk.PhotoImage(bg_image)
bg_label = Label(root, image=bg_photo)
bg_label.place(relwidth=1, relheight=1)

# Создание текстовых полей для ввода state и details
state_label = Label(root, text="State:")
state_label.pack()
state_entry = Entry(root)
state_entry.pack()

details_label = Label(root, text="Details:")
details_label.pack()
details_entry = Entry(root)
details_entry.pack()

# Создание кнопок для выбора переменной choose
choose_var = IntVar()
choose_var.set(1)

choose_label = Label(root, text="Choose:")
choose_label.pack()

radio_gawr_gura = Radiobutton(root, text="GawrGura", variable=choose_var, value=1, command=select_choose)
radio_ayaka = Radiobutton(root, text="Ayaka", variable=choose_var, value=2, command=select_choose)
radio_hu_tao = Radiobutton(root, text="Hu Tao", variable=choose_var, value=3, command=select_choose)
radio_vampire = Radiobutton(root, text="Vampire", variable=choose_var, value=4, command=select_choose)

radio_gawr_gura.pack()
radio_ayaka.pack()
radio_hu_tao.pack()
radio_vampire.pack()

# Создание кнопок для управления RPC
start_button = Button(root, text="Start", command=Start)
stop_button = Button(root, text="Stop", command=root.quit)

start_button.pack()
stop_button.pack()

root.mainloop()