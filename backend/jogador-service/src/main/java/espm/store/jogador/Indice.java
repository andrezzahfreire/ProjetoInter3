package espm.store.jogador;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;
import lombok.experimental.Accessors;

@Getter @Setter @ToString
@Builder @Accessors(chain = true, fluent = true)
@NoArgsConstructor @AllArgsConstructor
public class Indice {

    private String id;
    private Jogador jogador;

    private String nome;
    private Double valor;
    private String texto;

}
