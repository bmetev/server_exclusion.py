# Create list:
server_name = input()

servers_list = [server_name]

while not server_name == "end":
    server_name = input()
    servers_list.append(server_name)

servers_list.remove(servers_list[-1])

print(servers_list)

# Remove from the list:

server_remove = input()

while not server_remove == "stop":

    servers_list.remove(server_remove)
    server_remove = input()

print(servers_list)