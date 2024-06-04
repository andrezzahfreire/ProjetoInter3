package espm.store.jogador;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity
@Getter
@Setter
@Table(name = "indice")
@AllArgsConstructor
@NoArgsConstructor
public class IndiceModel {

    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    @Column(name = "id_indice")
    private String id;

    @Column(name = "id_jogador")
    private String jogador;

    @Column(name = "nome")
    private String nome;

    @Column(name = "valor")
    private Double valor;

    @Column(name = "texto")
    private String texto;

    public IndiceModel(Indice indice) {
        this.id = indice.id();
        this.jogador = indice.jogador().id();
        this.nome = indice.nome();
        this.valor = indice.valor();
        this.texto = indice.texto();
    }

    public Indice to() {
        return new Indice()
                .id(id)
                .jogador(new Jogador().id(jogador))
                .nome(nome)
                .valor(valor)
                .texto(texto);
    }
}
