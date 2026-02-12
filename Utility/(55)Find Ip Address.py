import socket
# The following code retrieves the local IP address of the current machine:
# 1. Use 'socket.gethostname()' to get the local hostname.
# 2. Use 'socket.gethostbyname_ex()' to get a list of IP addresses associated with the hostname.
# 3. Filter the list to exclude any IP addresses starting with "127." (loopback addresses).
# 4. Extract the first IP address (if available) from the filtered list.
# 5. Print the obtained IP address to the console.

local_hostname = socket.gethostname()

ip_addresses = socket.gethostbyname_ex(local_hostname)[2]

filtered_ips = [ip for ip in ip_addresses if not ip.startswith("127.")]

first_ip = filtered_ips[:1]


print(first_ip[0])