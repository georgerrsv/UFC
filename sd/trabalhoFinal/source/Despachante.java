import java.util.Map;
import java.sql.Connection;

public class Despachante {
    public String invoke(String message, Connection connection) {
        if (message.startsWith("Adicionar")) {
            // Chame o método apropriado no Esqueleto e retorne o resultado.
            Esqueleto esqueleto = new Esqueleto();
            return esqueleto.adicionarFilme(message);
        } else if (message.startsWith("Remover")) {
            // Chame o método apropriado no Esqueleto e retorne o resultado.
            Esqueleto esqueleto = new Esqueleto();
            return esqueleto.removerFilme(message);
        } else if (message.startsWith("ExibirDetalhe")) {
            // Chame o método apropriado no Esqueleto e retorne o resultado.
            Esqueleto esqueleto = new Esqueleto();
            return esqueleto.exibirDetalhe(message);
        } else if (message.equals("MostrarCatalogo")) {
            // Chame o método apropriado no Esqueleto
            Esqueleto esqueleto = new Esqueleto();
            Map<Integer, String> catalogo = esqueleto.mostrarCatalogo();

            // Converta o catálogo em uma representação de String
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
