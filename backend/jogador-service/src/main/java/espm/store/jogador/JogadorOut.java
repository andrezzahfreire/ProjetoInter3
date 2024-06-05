package espm.store.jogador;

import java.util.Map;

import lombok.Builder;
import lombok.experimental.Accessors;

@Builder @Accessors(fluent=true, chain=true)
public record JogadorOut (
    String id,
    String jogador,
    String nacionalidade,
    String posicao,
    String equipe,
    Integer idade,
    Integer nascimento,
    Map<String, Object> indices
) { }
