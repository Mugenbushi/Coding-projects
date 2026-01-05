import socket
import threading
from queue import Queue

def get_banner(target, port):
    #trying to grab the banner of the port to know service
    try:
        Bs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Bs.settimeout(3)
        Bs.connect((target, port))

        #some services will send the banner right away other need to have a request made 
        try:
            #attempting to receive banner with req
            banner = Bs.recv(1024).decode().strip()
            if banner:
                return banner
        except:
            pass
        #no banner try sending http request to receive the banner
        if port in [80, 443, 8080, 8000]:
            Bs.send(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n")
            banner = Bs.recv(1024).decode().strip()
            return banner
        
        Bs.close()
        return None
    except:
        return None

def port_scanner(target, port):
    try:
        # Basic to always get the socket started
        Ps = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Ps.settimeout(1) #sets the time out for the port probe
        result = Ps.connect_ex((target, port))  # Note the tuple!  #RETURNS 0 If open

        if result == 0:
            print(f" Port:{port} is OPEN", end="")
            # Try to detect service 
            banner = get_banner(target, port)
            if banner:
                #shows the 100 characters of the banner
                service = banner[:100].replace("\n", " ").replace("\r", "")
                print(f" -> {service}")
            else:
                print(" -> Unknown service!")
        # Removed else to reduce output clutter with threading
        
        Ps.close()
    except socket.gaierror:
        print("Hostname could not be resolved")
    except socket.timeout:
        print(f"Port {port}: TIMEOUT (filtered/slow)")
    except Exception as e:
        print(f"Port {port}: ERROR - {e}")

# Multi-threading function
def threaded_scanner(target, port_queue, lock):
    """Worker thread that scans ports from the queue"""
    while True:
        port = port_queue.get()
        if port is None:  # Poison pill to stop thread
            break
        
        # Use lock to prevent print statements from overlapping
        with lock:
            port_scanner(target, port)
        
        port_queue.task_done()

def scan_ports_threaded(target, ports, num_threads=10):
    """Main function to coordinate threaded scanning"""
    port_queue = Queue()
    lock = threading.Lock()
    
    # Create and start worker threads
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=threaded_scanner, args=(target, port_queue, lock))
        thread.daemon = True  # Thread dies when main program exits
        thread.start()
        threads.append(thread)
    
    # Add all ports to the queue
    for port in ports:
        port_queue.put(port)
    
    # Wait for all ports to be scanned
    port_queue.join()
    
    # Stop all threads
    for _ in range(num_threads):
        port_queue.put(None)
    
    for thread in threads:
        thread.join()

# Usage
target = "scanme.nmap.org"
common_ports = [21, 22, 25, 80, 443, 3306, 5432, 8080]

print(f"Scanning {target} with multi-threading...\n")
scan_ports_threaded(target, common_ports, num_threads=10)

print("\n[+] Scan complete!")