import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class UDPServer {
    private static final int PORT = 12345;
    private static final String DB_URL = "jdbc:postgresql://localhost:5432/filme";
    private static final String DB_USER = "admin";
    private static final String DB_PASSWORD = "admin";
    private Connection connection;

    public UDPServer() {
        // Estabelecer a conexão com o banco de dados no construtor
        try {
            connection = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
            System.out.println("Conexão com o banco de dados estabelecida.");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public String getRequest(String request) {
        // Implemente a lógica de processamento da solicitação
        // e a interação com o banco de dados, se necessário

        Despachante despachante = new Despachante();
        String response = despachante.invoke(request, connection);
        return response;
    }

    public void sendResponse(String response, InetAddress clientAddress, int clientPort) {
        byte[] responseData = response.getBytes();

        try (DatagramSocket serverSocket = new DatagramSocket()) {
            DatagramPacket sendPacket = new DatagramPacket(responseData, responseData.length, clientAddress, clientPort);
            serverSocket.send(sendPacket);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        UDPServer server = new UDPServer();

        try (DatagramSocket serverSocket = new DatagramSocket(PORT)) {
            System.out.println("Servidor UDP iniciado. Establecendo conexão...");

            while (true) {
                byte[] receiveData = new byte[1024];
                DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
                serverSocket.receive(receivePacket);

                String request = new String(receivePacket.getData(), 0, receivePacket.getLength());
                String response = server.getRequest(request);
                InetAddress clientAddress = receivePacket.getAddress();
                int clientPort = receivePacket.getPort();

                server.sendResponse(response, clientAddress, clientPort);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
