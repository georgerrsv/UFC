package org.example;
import java.sql.SQLException;

public class Esqueleto {
    private Database db;

    public Esqueleto(Database db) throws SQLException {
        this.db = db;
    }

    public String adicionarFilme(String arguments) throws SQLException {
        Filme filme = Filme.fromJson(arguments);
        return db.adicionarFilme(filme);
    }

    public String removerFilme(String arguments) throws SQLException {
        return db.removerFilme(Integer.parseInt(arguments));
    }

    public String exibirDetalhe(String arguments) throws SQLException {
        return db.exibirDetalhe(Integer.parseInt(arguments));
    }

    public String mostrarCatalogo() throws SQLException {
        return db.mostrarCatalogo();
    }
}
