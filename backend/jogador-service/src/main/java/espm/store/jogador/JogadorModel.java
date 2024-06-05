package espm.store.jogador;

import java.util.ArrayList;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

/*
 * Representa a tabela de contas de usuários
 */
@Entity
@Getter @Setter
@Table(name ="jogador")
@AllArgsConstructor @NoArgsConstructor
public class JogadorModel {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    @Column(name = "id_jogador")
    private String id;

    @Column(name = "jogador")
    private String jogador;

    @Column(name = "nacionalidade")
    private String nacionalidade;

    @Column(name = "posicao")
    private String posicao;

    @Column(name = "equipe")
    private String equipe;

    @Column(name = "idade")
    private Integer idade;

    @Column(name = "nascimento")
    private Integer nascimento;

    public JogadorModel(Jogador account) {
        this.id = account.id();
        this.jogador = account.jogador();
        this.nacionalidade = account.nacionalidade();
        this.posicao = account.posicao();
        this.equipe = account.equipe();
        this.idade = account.idade();
        this.nascimento = account.nascimento();
    }

    public Jogador to() {
        return new Jogador()
            .id(id)
            .jogador(jogador)
            .nacionalidade(nacionalidade)
            .posicao(posicao)
            .equipe(equipe)
            .idade(idade)
            .nascimento(nascimento)
            .indices(new ArrayList<>());
    }
}
