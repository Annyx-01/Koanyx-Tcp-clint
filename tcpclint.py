import socket

# ANSI color codes
MAHOGANY = '\033[38;2;192;64;0m'  # RGB: 192,64,0 - Mahogany brown
RESET = '\033[0m'  # Resets color back to normal

# BANNER - Shows first when program starts in MAHOGANY color
BANNER = f"""
{MAHOGANY}
██╗  ██╗ ██████╗  █████╗ ███╗   ██╗██╗   ██╗██╗  ██╗
██║ ██╔╝██╔═══██╗██╔══██╗████╗  ██║╚██╗ ██╔╝╚██╗██╔╝
█████╔╝ ██║   ██║███████║██╔██╗ ██║ ╚████╔╝  ╚███╔╝ 
██╔═██╗ ██║   ██║██╔══██║██║╚██╗██║  ╚██╔╝   ██╔██╗ 
██║  ██╗╚██████╔╝██║  ██║██║ ╚████║   ██║   ██╔╝ ██╗
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝                                
                    TCP CLIENT
====================================================={RESET}
"""

def tcp_client(host, port, message):
    """
    A flexible TCP client that can connect to any host and port
    """
    try:
        # Create a socket object
        # AF_INET = IPv4, SOCK_STREAM = TCP
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set timeout (optional, prevents hanging)
        client.settimeout(5)
        
        # Connect to the server
        print(f"[*] Connecting to {host}:{port}")
        client.connect((host, port))
        
        # Send data
        print(f"[*] Sending data: {message}")
        client.send(message.encode() if isinstance(message, str) else message)
        
        # Receive response
        response = b""
        while True:
            try:
                data = client.recv(4096)
                if not data:
                    break
                response += data
            except socket.timeout:
                break
        
        # Print response
        print("[*] Response received:")
        print(response.decode('utf-8', errors='ignore'))
        
        # Close connection
        client.close()
        
    except socket.error as e:
        print(f"[-] Socket error: {e}")
    except Exception as e:
        print(f"[-] Error: {e}")

# Print banner FIRST before anything else (in mahogany brown)
print(BANNER)

# Get input from user
if __name__ == "__main__":
    print("=== TCP Client ===")
    
    # Get website/host from user
    target_host = input("Enter website name (e.g., google.com): ").strip()
    
    # Get port from user
    try:
        target_port = int(input("Enter port number (e.g., 80 for HTTP): ").strip())
    except ValueError:
        print("[-] Invalid port number. Using default port 80.")
        target_port = 80
    
    # Get message/data to send
    print("\nWhat would you like to send?")
    print("1. HTTP GET request (default)")
    print("2. Custom message")
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == "2":
        message = input("Enter your custom message: ")
    else:
        # Create a basic HTTP request
        message = f"GET / HTTP/1.1\r\nHost: {target_host}\r\nConnection: close\r\n\r\n"
        print(f"[*] Using HTTP GET request for {target_host}")
    
    print("\n" + "="*40)
    # Call the function
    tcp_client(target_host, target_port, message)
    
    # Optional: Ask if user wants to try another connection
    print("\n" + "="*40)
    again = input("Do you want to try another connection? (y/n): ").strip().lower()
    if again == 'y':
        print("Run the script again to test another connection!")