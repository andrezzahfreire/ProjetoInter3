package espm.store.jogador;

import java.util.List;

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
public final class Jogador {

    private String id;
    private String jogador;  
    private String nacionalidade;
    private String posicao;  
    private String equipe;  
    private Integer idade; 
    private Integer nascimento;
    private List<Indice> indices;

}
