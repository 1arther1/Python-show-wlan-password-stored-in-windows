import os
def timer():
    import time
    t = 3
    print ("akan berlangsung 3 detik")
    while (t >= 0):
        print (t, end='...')
        time.sleep(1)
        t -= 1
        print ('') 
timer()
lagi = True
while(lagi == True):
    os.system("netsh wlan show profiles")
    a = input("masukkan nama ssid untuk lihat password : ")
    os.system('netsh wlan show profiles name="{}" key=clear'.format(a))
    
    while True:
        g = input("ingin lihat lagi (t/y) ?  ")
        if (g == "t"):
            lagi = False
        elif (g == "y"):
            break
        else:
            print("input salah")
            
        break
            