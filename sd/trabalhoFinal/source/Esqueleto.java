import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.HashMap;
import java.util.Map;

public class Esqueleto {
    private static final String DB_URL = "jdbc:postgresql://localhost:5432/seu_banco_de_dados";
    private static final String DB_USER = "seu_usuario";
    private static final String DB_PASSWORD = "sua_senha";

    public String adicionarFilme(String request) {
        try {
            Connection connection = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
            String[] params = request.split(",");
            if (params.length != 8) {
                connection.close();
                return "Parâmetros inválidos.";
            }

            String sql = "INSERT INTO filme(id, titulo, diretor, ano, duracao, genero, classificacao, descricao) " +
                    "VALUES(?, ?, ?, ?, ?, ?, ?, ?)";
            PreparedStatement statement = connection.prepareStatement(sql);
            statement.setInt(1, Integer.parseInt(params[1]));
            statement.setString(2, params[2]);
            statement.setString(3, params[3]);
            statement.setInt(4, Integer.parseInt(params[4]));
            statement.setInt(5, Integer.parseInt(params[5]));
            statement.setString(6, params[6]);
            statement.setString(7, params[7]);
            statement.setString(8, params[8]);

            int rowsInserted = statement.executeUpdate();
            statement.close();
            connection.close();

            if (rowsInserted > 0) {
                return "Filme adicionado com sucesso.";
            } else {
                return "Erro ao adicionar filme.";
            }
        } catch (SQLException e) {
            e.printStackTrace();
            return "Erro no banco de dados.";
        }
    }

    public String removerFilme(String request) {
        try {
            Connection connection = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
            int id = Integer.parseInt(request.split(",")[1]);
            String sql = "DELETE FROM filme WHERE id = ?";
            PreparedStatement statement = connection.prepareStatement(sql);
            statement.setInt(1, id);

            int rowsDeleted = statement.executeUpdate();
            statement.close();
            connection.close();

            if (rowsDeleted > 0) {
                return "Filme removido com sucesso.";
            } else {
                return "Erro ao remover filme.";
            }
        } catch (SQLException e) {
            e.printStackTrace();
            return "Erro no banco de dados.";
        }
    }

    public String exibirDetalhe(String request) {
        try {
            Connection connection = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
            int id = Integer.parseInt(request.split(",")[1]);
            String sql = "SELECT * FROM filme WHERE id = ?";
            PreparedStatement statement = connection.prepareStatement(sql);
            statement.setInt(1, id);
            ResultSet resultSet = statement.executeQuery();

            if (resultSet.next()) {
                String detalhes = "ID: " + resultSet.getInt("id") + "\n" +
                        "Título: " + resultSet.getString("titulo") + "\n" +
                        "Diretor: " + resultSet.getString("diretor") + "\n" +
                        "Ano: " + resultSet.getInt("ano") + "\n" +
                        "Duração: " + resultSet.getInt("duracao") + " minutos\n" +
                        "Gênero: " + resultSet.getString("genero") + "\n" +
                        "Classificação: " + resultSet.getString("classificacao") + "\n" +
                        "Descrição: " + resultSet.getString("descricao");
                resultSet.close();
                statement.close();
                connection.close();
                return detalhes;
            } else {
                resultSet.close();
                statement.close();
                connection.close();
                return "Filme não encontrado.";
            }
        } catch (SQLException e) {
            e.printStackTrace();
            return "Erro no banco de dados.";
        }
    }

    public Map<Integer, String> mostrarCatalogo() {
        Map<Integer, String> catalogo = new HashMap<>();
        try {
            Connection connection = DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
            String sql = "SELECT id, titulo FROM filme";
            PreparedStatement statement = connection.prepareStatement(sql);
            ResultSet resultSet = statement.executeQuery();

            while (resultSet.next()) {
                int id = resultSet.getInt("id");
                String titulo = resultSet.getString("titulo");
                catalogo.put(id, titulo);
            }

            resultSet.close();
            statement.close();
            connection.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return catalogo;
    }
}
