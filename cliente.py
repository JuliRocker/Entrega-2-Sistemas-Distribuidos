import socket

def iniciar_cliente():
    HOST = '192.168.10.1'  # IP de nfs-server
    PORT = 5000            # Puerto TCP de servicio
    
    try:
        # Crea el socket y se conecta al servidor
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        print("=== CONEXIÓN ESTABLECIDA CON EL SERVIDOR DE DIRECTORIO ===")
        
        # Realiza las 2 consultas requeridas por la guía
        for i in range(1, 3):
            print(f"\n--- Consulta #{i} ---")
            telefono = input("Ingrese el número telefónico a consultar: ")
            
            client_socket.sendall(telefono.encode('utf-8'))
            respuesta = client_socket.recv(1024).decode('utf-8')
            
            print(f"\n[Respuesta Servidor]: {respuesta}\n")
            
        # Finaliza la transacción
        client_socket.sendall("salir".encode('utf-8'))
        client_socket.close()
        print("=== Transacción finalizada exitosamente. Socket cliente cerrado. ===")
        
    except Exception as e:
        print(f"Error de conexión: {e}")

if __name__ == '__main__':
    iniciar_cliente()
