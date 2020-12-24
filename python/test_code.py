import requests
import threading
import asyncio
from tqdm import tqdm
from datetime import datetime

async def send(vdata):
    # prc = tqdm(total=10,desc=f"starting {vdata}: ")
    stti = datetime.now()
    # url = "http://superapp.minerva.vn:9218/api/be/v1/project/"
    url = "http://172.18.210.154:1234/api/be/v1/project/"
    payload={}
    headers = {
        'Content-Type': 'application/json',
        'MNV-ENCODE': '0',
        'Authorization': 'Bearer MjoxMzliMDZiZmI4OTJhOGYxYmQ2MzVhZmFmODEyZmM5M2RhNDFkM2Yx'
    }
    # prc.update(2)
    
    res = requests.request("GET", url, headers=headers, data=payload)
    if res.status_code == 200:
        print(datetime.now() - stti, "-- True")
    else:
        print(datetime.now() - stti, "-- False")
    # print(response.text)
    
    # prc.update(8)
    # prc.close()
    # print(f"success: {vdata}")

async def share_con(start):
    conn = []
    for temp in range(1000):
        conn.append(asyncio.create_task(send(start + temp)))
    await asyncio.gather(*conn)

if __name__=="__main__":
    list_thd = []
    for temp in range(50):
        kwargs = {
            "vdata":temp
        }
        a = share_con(temp)
        thd = threading.Thread(target=asyncio.run,args=[a])
        thd.start()
        # thd.Lock()
        list_thd.append(thd)
    print(threading.active_count())
    for temp in list_thd:
        temp.join()


