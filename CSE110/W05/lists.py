clients = []

clients.append("John")
clients.append("Mary")

new_client = input("New client name: ")
clients.append(new_client)

for client in clients:
    print(client)