import java.util.Map;
import java.sql.Connection;

public class Despachante {
    public String invoke(String message, Connection connection) {
        if (message.startsWith("Adicionar")) {

            Esqueleto esqueleto = new Esqueleto();
            return esqueleto.adicionarFilme(message);
        } else if (message.startsWith("Remover")) {
            
            Esqueleto esqueleto = new Esqueleto();
            return esqueleto.removerFilme(message);
        } else if (message.startsWith("ExibirDetalhe")) {
            
            Esqueleto esqueleto = new Esqueleto();
            return esqueleto.exibirDetalhe(message);
        } else if (message.equals("MostrarCatalogo")) {
            
            Esqueleto esqueleto = new Esqueleto();
            Map<Integer, String> catalogo = esqueleto.mostrarCatalogo();

            StringBuilder catalogoString = new StringBuilder();
            for (Map.Entry<Integer, String> entry : catalogo.entrySet()) {
                catalogoString.append("ID: ").append(entry.getKey()).append(", Título: ").append(entry.getValue()).append("\n");
            }

            return catalogoString.toString();
        } else {
            return "Comando inválido.";
        }
    }
}
