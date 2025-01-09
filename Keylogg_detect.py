import psutil
import sys

def main():
    print("Listing all running processes with network connections and loaded modules.\n")
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            p = psutil.Process(proc.pid)
            print(f"Process: {p.name()} (PID: {p.pid})")
            print(f"User: {p.username()}")
            print("Loaded Modules:")
            for module in p.memory_maps():
                print(f"  {module.path}")
            print("Network Connections:")
            for conn in p.connections():
                print(f"  {conn.laddr} -> {conn.raddr}")
            print("-" * 40)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

if __name__ == "__main__":
    main()
