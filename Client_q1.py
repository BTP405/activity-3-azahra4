import socket
import pickle

def send_file(file_path, server_host, server_port):
    #BUFFER_SIZE = 1024

    with open(file_path, 'rb') as f:
        file_content = f.read()

    file_name = file_path.split('/')[-1]
    file_object = {'filename': file_name, 'content': file_content}
    pickled_data = pickle.dumps(file_object) #Convert the file_data from python object to byte string

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_host, server_port))
    client_socket.sendall(pickled_data)
    client_socket.close()

def main():
    SERVER_HOST = '127.0.0.1'
    SERVER_PORT = 27000

    file_path = input("Enter the path of the file to transfer: ")

    try:
        send_file(file_path, SERVER_HOST, SERVER_PORT)
        print("File successfully sent to the server.")
    except FileNotFoundError:
        print("Error: File not found.")
    except IOError as e:
        print("Error: Unable to send file:", e)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
