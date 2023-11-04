package org.example;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import org.json.JSONArray;
import org.json.JSONObject;

public class Database {
    private Connection connection;
    private PreparedStatement preparedStatement;

    public Database() throws SQLException {
        connection = DriverManager.getConnection(
                "jdbc:postgresql://localhost/filme",
                "postgres",
                "admin"
        );
    }

    public String adicionarFilme(Filme filme) throws SQLException {
        preparedStatement = connection.prepareStatement("INSERT INTO filme (titulo, diretor, ano, duracao, genero, classificacao, descricao) VALUES (?, ?, ?, ?, ?, ?, ?)");
        preparedStatement.setString(1, filme.getTitulo());
        preparedStatement.setString(2, filme.getDiretor());
        preparedStatement.setInt(3, filme.getAno());
        preparedStatement.setInt(4, filme.getDuracao());
        preparedStatement.setString(5, filme.getGenero());
        preparedStatement.setInt(6, filme.getClassificacao());
        preparedStatement.setString(7, filme.getDescricao());

        int rowsAffected = preparedStatement.executeUpdate();

        if (rowsAffected == 1) {
            return "Filme cadastrado com sucesso!";
        } else {
            return "Erro ao cadastrar filme!";
        }
    }

    public String removerFilme(int id) throws SQLException {
        preparedStatement = connection.prepareStatement("DELETE FROM filme WHERE id = ?");
        preparedStatement.setInt(1, id);

        int rowsAffected = preparedStatement.executeUpdate();

        if (rowsAffected == 1) {
            return "Filme removido com sucesso!";
        } else {
            return "Erro ao remover filme!";
        }
    }

    public String exibirDetalhe(int id) throws SQLException {
        preparedStatement = connection.prepareStatement("SELECT * FROM filme WHERE id = ?");
        preparedStatement.setInt(1, id);

        ResultSet resultSet = preparedStatement.executeQuery();

        if (resultSet.next()) {
            String titulo = resultSet.getString("titulo");
            String diretor = resultSet.getString("diretor");
            int ano = resultSet.getInt("ano");
            int duracao = resultSet.getInt("duracao");
            String genero = resultSet.getString("genero");
            int classificacao = resultSet.getInt("classificacao");
            String descricao = resultSet.getString("descricao");

            return new Filme(titulo, diretor, ano, duracao, genero, classificacao, descricao).toJson();
        } else {
            return null;
        }
    }

    public String mostrarCatalogo() throws SQLException {
        preparedStatement = connection.prepareStatement("SELECT id, titulo FROM filme");
        ResultSet resultSet = preparedStatement.executeQuery();

        List<JSONObject> catalogo = new ArrayList<>();

        while (resultSet.next()) {
            int id = resultSet.getInt("id");
            String titulo = resultSet.getString("titulo");

            JSONObject filme = new JSONObject();
            filme.put("id", id);
            filme.put("titulo", titulo);

            catalogo.add(filme);
        }

        String catalogoJSON = new JSONArray(catalogo).toString();

        return catalogoJSON;
    }

}
