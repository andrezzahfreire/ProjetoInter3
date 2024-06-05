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

    public String id;
    public String jogador;  
    public String nacionalidade;
    public String posicao;  
    public String equipe;  
    public Integer idade; 
    public Integer nascimento;
    public List<Indice> indices;

}
