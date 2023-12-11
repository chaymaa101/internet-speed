import math
import speedtest
def conversion_B_MB(size_bytes):
    i=int(math.floor(math.log(size_bytes,1024)))
    power=math.pow(1023,i)
    size=round(size_bytes/power,2)
    return f"{size} Mpbs"

# We create a Speedtest object
wifi =speedtest.Speedtest()

print("Getting download speed...")
download_speed=wifi.download()

print("getting upload speed...")
upload_speed=wifi.upload()

#print("Download: ",download_speed)
#print("Upload: ",upload_speed)

print("Download: ",conversion_B_MB(download_speed))
print("Upload: ",conversion_B_MB(upload_speed))