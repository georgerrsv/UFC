package org.example;
import java.io.*;
import java.net.*;
import java.sql.SQLException;
import org.json.JSONObject;

public class UDPServer {
    private DatagramSocket serverSocket;
    private final Database db;

    public UDPServer(int port) throws SocketException, SQLException {
        this.serverSocket = new DatagramSocket(port);
        this.db = new Database();
    }

    public void getRequest() throws IOException, SQLException {
        byte[] receiveData = new byte[1024];
        DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
        serverSocket.receive(receivePacket);
        String data = new String(receivePacket.getData(), 0, receivePacket.getLength(), "UTF-8");

        try {
            JSONObject requestJson = new JSONObject(data);
            String objectReference = requestJson.getString("objectreference");
            int methodId = requestJson.getInt("methodId");
            String arguments = requestJson.getString("arguments");

            Despachante despachante = new Despachante(db);
            String response = despachante.invoke(objectReference, methodId, arguments);

            JSONObject responseJson = new JSONObject();
            responseJson.put("messageType", 0);
            responseJson.put("objectreference", objectReference);
            responseJson.put("methodId", methodId);
            responseJson.put("arguments", response);

            String responseStr = responseJson.toString();
            InetAddress clientAddress = receivePacket.getAddress();
            int clientPort = receivePacket.getPort();
            byte[] sendData = responseStr.getBytes("UTF-8");
            DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, clientAddress, clientPort);
            serverSocket.send(sendPacket);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) throws Exception {
        UDPServer server = new UDPServer(8080);
        System.out.println("Servidor UDP iniciado. Aguardando conexões...");
        while (true) {
            server.getRequest();
        }
    }
}
