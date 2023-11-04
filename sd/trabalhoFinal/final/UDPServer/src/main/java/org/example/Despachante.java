package org.example;
import org.json.JSONException;
import org.json.JSONObject;
import java.sql.SQLException;

public class Despachante {
    private Esqueleto esqueleto;

    public Despachante(Database db) throws SQLException {
        this.esqueleto = new Esqueleto(db);
    }

    public String invoke(String objectReference, int methodId, String arguments) {
        try {
            String response;
            if (methodId == 1) {
                response = esqueleto.adicionarFilme(arguments);
            } else if (methodId == 2) {
                response = esqueleto.removerFilme(arguments);
            } else if (methodId == 3) {
                response = esqueleto.exibirDetalhe(arguments);
            } else if (methodId == 4) {
                response = esqueleto.mostrarCatalogo();
            } else {
                response = "Método não reconhecido";
            }

            return response;
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
}
