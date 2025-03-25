-- Criação da tabela alunos
CREATE TABLE alunos (
    aluno_id CHARACTER VARYING(5) NOT NULL,
    nome CHARACTER VARYING(40) NOT NULL,
    endereco CHARACTER VARYING(60),
    cidade CHARACTER VARYING(15),
    estado CHARACTER VARYING(15),
    cep CHARACTER VARYING(10),
    pais CHARACTER VARYING(15),
    telefone CHARACTER VARYING(24),
    PRIMARY KEY (aluno_id)
);

-- Inserindo 10 registros na tabela alunos
INSERT INTO alunos (aluno_id, nome, endereco, cidade, estado, cep, pais, telefone) VALUES
('A001', 'João Silva', 'Rua das Flores, 123', 'São Paulo', 'SP', '01234-567', 'Brasil', '11987654321'),
('A002', 'Maria Oliveira', 'Av. Paulista, 1000', 'São Paulo', 'SP', '01310-100', 'Brasil', '11991234567'),
('A003', 'Pedro Santos', 'Rua Nova, 50', 'Rio de Janeiro', 'RJ', '22020-001', 'Brasil', '21987654321'),
('A004', 'Ana Souza', 'Rua Central, 456', 'Curitiba', 'PR', '80000-000', 'Brasil', '41912345678'),
('A005', 'Carlos Lima', 'Av. Brasil, 789', 'Belo Horizonte', 'MG', '30110-090', 'Brasil', '31987654321'),
('A006', 'Fernanda Rocha', 'Rua Alameda, 234', 'Porto Alegre', 'RS', '90000-001', 'Brasil', '51912345678'),
('A007', 'Paulo Castro', 'Av. Independência, 345', 'Salvador', 'BA', '40000-000', 'Brasil', '71987654321'),
('A008', 'Clara Mendes', 'Rua Verde, 123', 'Recife', 'PE', '50000-000', 'Brasil', '81912345678'),
('A009', 'Roberto Nunes', 'Av. Mar, 456', 'Fortaleza', 'CE', '60000-000', 'Brasil', '85987654321'),
('A010', 'Juliana Alves', 'Rua do Sol, 789', 'Manaus', 'AM', '69000-000', 'Brasil', '92912345678');
