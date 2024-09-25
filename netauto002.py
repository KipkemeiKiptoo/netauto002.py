import ping3
import csv
import time


devices = ["192.168.1.1", "google.com", "192.168.1.2"]


with open('ping_latency.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(["Device", "Ping Status", "Latency (ms)", "Timestamp"])

  
    for device in devices:
        try:
            
            latency = ping3.ping(device, timeout=2)
            
            if latency is None:
                print(f"Device {device} is unreachable.")
                writer.writerow([device, "Unreachable", "-", time.strftime('%Y-%m-%d %H:%M:%S')])
            else:
               
                latency_ms = round(latency * 1000, 2)
                print(f"Device {device} responded in {latency_ms} ms.")
                writer.writerow([device, "Reachable", latency_ms, time.strftime('%Y-%m-%d %H:%M:%S')])

        except Exception as e:
            
            print(f"Error pinging device {device}: {e}")
            writer.writerow([device, "Error", "-", time.strftime('%Y-%m-%d %H:%M:%S')])

print("Ping test completed. Latency data recorded in ping_latency.csv.")
