#include <iostream>
#include <map>
#include <sstream>
#include <list>
#include <memory>

class Aluno {
    std::string id;
    std::map<std::string, Discp> disciplinas;

public:
    Aluno(std::string id) {
        this->id = id;
    }

    std::string getId() const {
        return this->id;
    }

    std::list<Discp> getDisciplinas() const {
        std::list<Discp> lista;
        for (auto& par : this->disciplinas) {
            lista.push_back(par.second);
        }
        return lista;
    }

    void addDisciplina(Discp disciplina) {
        this->disciplinas[disciplina.getId()] = disciplina;
    }

    void rmvDisciplina(Discp disciplina) {
        this->disciplinas.erase(disciplina.getId());
    }

    std::string toString() const {
        std::ostringstream oss;
        oss << this->id << " - " << this->disciplinas.size() << " disciplinas";
        return oss.str();
    }
};

std::ostream& operator<<(std::ostream& os, const Aluno& aluno) {
    os << aluno.toString();
    return os;
}

class Discp {
    std::string id;
    std::map<std::string, Aluno> alunos;

public:
    Discp(std::string id) {
        this->id = id;
    }

    std::string getId() const {
        return this->id;
    }

    std::list<Aluno> getAlunos() const {
        std::list<Aluno> lista;
        for (auto& par : this->alunos) {
            lista.push_back(par.second);
        }
        return lista;
    }

    void addAluno(Aluno aluno) {
        this->alunos[aluno.getId()] = aluno;
    }

    void rmvAluno(Aluno aluno) {
        this->alunos.erase(aluno.getId());
    }

    std::string toString() const {
        std::ostringstream oss;
        oss << this->id << " - " << this->alunos.size() << " alunos";
        return oss.str();
    }
};

std::ostream& operator<<(std::ostream& os, const Discp& disciplina) {
    os << disciplina.toString();
    return os;
}

class System {
    std::map<std::string, Aluno> alunos;
    std::map<std::string, Discp> disciplinas;

public:
    System() {}

    void addAluno(Aluno aluno) {
        this->alunos[aluno.getId()] = aluno;
    }

    void addDisciplina(Discp disciplina) {
        this->disciplinas[disciplina.getId()] = disciplina;
    }

    std::list<Aluno> getAlunos() const {
        std::list<Aluno> lista;
        for (auto& par : this->alunos) {
            lista.push_back(par.second);
        }
        return lista;
    }

    std::list<Discp> getDisciplinas() const {
        std::list<Discp> lista;
        for (auto& par : this->disciplinas) {
            lista.push_back(par.second);
        }
        return lista;
    }

    void matricula(std::string alunoId, std::string discpId) {
        auto aluno = this->alunos[alunoId];
        auto disciplina = this->disciplinas[discpId];
        aluno.addDisciplina(disciplina);
        disciplina.addAluno(aluno);
    }

    void desmatricula(std::string alunoId, std::string discpId) {
        auto aluno = this->alunos[alunoId];
        auto disciplina = this->disciplinas[discpId];
        aluno.rmvDisciplina(disciplina);
        disciplina.rmvAluno(aluno);
    }

    void rmvAluno(std::string alunoId) {
        auto aluno = this->alunos[alunoId];
        for (auto& disciplina : aluno.getDisciplinas()) {
            disciplina.rmvAluno(aluno);
        }
        this->alunos.erase(alunoId);
    }

    void rmvDisciplina(std::string discpId) {
        auto disciplina = this->disciplinas[discpId];
        for (auto& aluno : disciplina.getAlunos()) {
            aluno.rmvDisciplina(disciplina);
        }
        this->disciplinas.erase(discpId);
    }

    std::string toString() const {
        std::ostringstream oss;
        oss << "Alunos:" << std::endl;
        for (auto& aluno : this->getAlunos()) {
            oss << aluno << std::endl;
        }
        oss << "Disciplinas:" << std::endl;
        for (auto& disciplina : this->getDisciplinas()) {
            oss << disciplina << std::endl;
        }
        return oss.str();
    }

    std::ostream& operator<<(std::ostream& os) {
        for (auto& aluno : this->getAlunos()) {
            os << aluno << std::endl;
        }
    }
};

std::ostream& operator<<(std::ostream& os, const System& system) {
    os << system.toString();
    return os;
}

int main() {
    System system;
    system.addAluno(Aluno("A1"));
    system.addAluno(Aluno("A2"));
    system.addAluno(Aluno("A3"));
    system.addDisciplina(Discp("D1"));
    system.addDisciplina(Discp("D2"));
    system.addDisciplina(Discp("D3"));
    system.matricula("A1", "D1");
    system.matricula("A1", "D2");
    system.matricula("A2", "D1");
    system.matricula("A2", "D2");
    system.matricula("A2", "D3");
    system.matricula("A3", "D1");
    system.matricula("A3", "D2");
    system.matricula("A3", "D3");
    std::cout << system << std::endl;
    system.desmatricula("A1", "D1");
    system.desmatricula("A2", "D1");
    system.desmatricula("A3", "D1");
    system.rmvAluno("A1");
    system.rmvDisciplina("D1");
    std::cout << system << std::endl;
    return 0;
}