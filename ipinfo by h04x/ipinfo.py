import requests
import os
banner = """

$$$$$$\ $$$$$$$\        $$$$$$\ $$\   $$\ $$$$$$$$\  $$$$$$\  
\_$$  _|$$  __$$\       \_$$  _|$$$\  $$ |$$  _____|$$  __$$\ 
  $$ |  $$ |  $$ |        $$ |  $$$$\ $$ |$$ |      $$ /  $$ |
  $$ |  $$$$$$$  |        $$ |  $$ $$\$$ |$$$$$\    $$ |  $$ |
  $$ |  $$  ____/         $$ |  $$ \$$$$ |$$  __|   $$ |  $$ |
  $$ |  $$ |              $$ |  $$ |\$$$ |$$ |      $$ |  $$ |
$$$$$$\ $$ |            $$$$$$\ $$ | \$$ |$$ |       $$$$$$  |
\______|\__|            \______|\__|  \__|\__|       \______/ 
                                                              
                                                              
                                                              
[BY H04X]
"""

os.system("cls")

print(banner)



ip = input("H04X/IP-Sorgu/IP Adresi Gir: ")

response = requests.post("http://ip-api.com/batch", json=[
  {"query": ip, "fields": "status,message,continent,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query"}
]).json()

for ip_info in response:
    for k,v in ip_info.items():
        print(k,v)
    print("\n"),