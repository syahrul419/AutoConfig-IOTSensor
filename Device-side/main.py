import listener 
import requests
import os
import time
import threading 

url = "http://172.168.0.133:8000/"
threads_list = []

#variabel untuk fungsi di dalam sw420.py
channel_getar = 17

def generateService(sensor):
    
    my_pass = "12345"
    service = """[Unit]
Description= {sensor_name} service
After=multi-user.target

[Service]
Environment=PYTHONUNBUFFERED=1
Type=simple
WorkingDirectory=/home/syahrul/skripsi/app
ExecStart=/usr/bin/python3 {sensor_name}/{sensor_name}.py
Restart=always
RestartSec=3

[Install]
WantedBy=multi-user.target
""".format(sensor_name=sensor)
    
    os.system("touch temporary_service_dir/"+sensor+".service")
    with open("temporary_service_dir/"+sensor+".service", 'w') as f:
        f.writelines(service)
        f.close()
        
    os.popen("sudo -S cp temporary_service_dir/"+sensor+".service /lib/systemd/system/"+sensor+".service", 'w').write(my_pass)
    os.system("sudo chmod 644 /lib/systemd/system/"+sensor+".service")
    os.system("sudo systemctl daemon-reload")
    os.system("sudo systemctl enable "+sensor+".service")
    os.system("sudo systemctl start "+sensor+".service")

def req_server(url, sensor, config ):
    r = requests.get(url)
    data = r.content
    status = r.status_code  
    print ("status:", status)
    #print(data)
    with open(sensor+"/"+config, 'wb') as f:
        f.write(data)

def get_Conf(sensor):
    global url
    
    start = time.perf_counter()
    requirements = "requirements.txt"
    
    #membuat directory penempatan konfigurasi
    if not os.path.isdir(sensor):
        os.makedirs(sensor)

    #untuk mengambil file requirements.txt dari server
    urlA = url + sensor +"/"+requirements
    req_server(urlA, sensor, requirements)
    os.system("pip3 install -r "+sensor+"/requirements.txt")

    #untuk mengambil file config yang baru		
    urlB = url + sensor +"/"+ sensor +".py"
    req_server(urlB, sensor, sensor+".py")
    
    #panggil fungsi generate service
    generateService(sensor)
    
    finish = time.perf_counter()
    print("[INFO] Konfigurasi selesai dilakukan!!!")
    print(f'[INFO] Autoconfig selesai dalam : {round(finish-start, 2)*1000} ms')

def get_suhu():
    while True:
        suhu_state = listener.suhu()
        print("[INFO] suhu :",suhu_state)
        if suhu_state == True:
            print("suhu terdeteksi")
            get_Conf("lm75a")
            break
        else:
            print("suhu belum terdeteksi")
            time.sleep(1)
            
def get_getar():
    global channel_getar
    while True:
        getar_state = listener.callback(channel_getar)
        print("[INFO] getar :",getar_state)
        if getar_state == True:
            print("getar terdeteksi")
            get_Conf("sw420")
            break
        else:
            print("getar belum terdeteksi")
            time.sleep(1)

def get_hujan():
    while True:
        hujan_state = listener.hujan()
        print("[INFO] hujan :",hujan_state)
        if hujan_state == True:
            print("hujan terdeteksi terdeteksi")
            get_Conf("hujan")
            break
        else:
            print("hujan belum terdeteksi")
            time.sleep(1)

def main():
    t1 = threading.Thread(target=get_suhu)
    threads_list.append(t1)

    t2 = threading.Thread(target=get_hujan)
    threads_list.append(t2)

    t3 = threading.Thread(target=get_getar)
    threads_list.append(t3)

    for t in threads_list:
        t.start()

    for t in threads_list:
        t.join()

if __name__ == "__main__":
    main() 	

