package espm.store.jogador;

import lombok.Builder;
import lombok.experimental.Accessors;

@Builder @Accessors(fluent=true, chain=true)
public record IndiceOut (
    String id,
    String nome,
    Object valor
) { }
