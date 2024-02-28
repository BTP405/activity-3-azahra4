import socket
import pickle

def save_file(file_data, save_path):
    with open(save_path, 'wb') as f:
        f.write(file_data)

def main():
    SERVER_HOST = '127.0.0.1' #Server ip-address
    SERVER_PORT = 27000 #Server's port where its listening
    BUFFER_SIZE = 1024 #The size of the info in the stream

    SAVE_DIR = './' #Save the file transferred into the current server folder 

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Setup the socket
    server_socket.bind((SERVER_HOST, SERVER_PORT)) #Bind the socket with port and ip
    server_socket.listen(1) #Make the socket available for listening

    print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}") #Print to the console that binding/listen are a success

    while True:
        client_socket, client_address = server_socket.accept() #Accept any client server with any address
        print(f"Connection from {client_address}") #Console to show accpet was successful

        file_data = b"" #an empty byte string initialized- Hold the data in byte string format so its ready to be sent
        while True:
            data = client_socket.recv(BUFFER_SIZE) #Recieve data coming from client
            if not data:
                break
            file_data += data

        try:
            file_object = pickle.loads(file_data) #UnPickle the byte string received from the client and save it into python object 
            file_name = file_object['filename']
            file_content = file_object['content']
            save_path = SAVE_DIR + file_name
            save_file(file_content, save_path)
            print(f"File saved to {save_path}")
        except pickle.UnpicklingError as e:
            print("Error: Unable to unpickle file object:", e)
        except IOError as e:
            print("Error: Unable to save file:", e)
        finally:
            client_socket.close()

if __name__ == "__main__":
    main()
