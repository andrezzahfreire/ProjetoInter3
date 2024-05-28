package espm.store.jogador;

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

@Entity
@Getter @Setter
@Table(name = "indice")
@AllArgsConstructor @NoArgsConstructor
public class IndiceModel {
    
    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    @Column(name = "id_indice")
    private String id;

    @Column(name = "id_jogador")
    private String idJogador;

    @Column(name = "nome")
    private String nome;

    @Column(name = "valor")
    private Double valor;

    @Column(name = "texto")
    private String texto;

    public IndiceModel(Indice indice) {
        this.id = indice.id();
        this.idJogador = indice.jogador().id();
        this.nome = indice.nome();
        this.valor = indice.valor();
        this.texto = indice.texto();
    }

    public Indice to() {
        return new Indice()
            .id(id)
            .jogador(new Jogador().id(idJogador))
            .nome(nome)
            .valor(valor)
            .texto(texto);
    }

}
