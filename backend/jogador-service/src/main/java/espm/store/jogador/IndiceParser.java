package espm.store.jogador;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public final class IndiceParser {
    
    public static List<Indice> to(Map<String, Object> in) {
        return in.entrySet().stream().map(entry -> {
            return to(entry.getKey(), entry.getValue());
        }).collect(Collectors.toList());
    }

    public static Indice to(String chave, Object valor) {
        return Indice.builder()
            .nome(chave)
            .valor(
                valor != null && (
                    Double.class.equals(valor.getClass()) || 
                    Integer.class.equals(valor.getClass())) ? 
                Double.parseDouble(String.valueOf(valor)) :
                null
            )
            .texto(
                valor != null && String.class.equals(valor.getClass()) ? 
                String.valueOf(valor) :
                null
            )
            .build();
    }

    public static Map<String, Object> to(List<Indice> ins) {
        Map<String, Object> indices = new HashMap<>();
        for (Indice indice : ins) {
            Object v = indice.texto() != null ? indice.texto() : indice.valor();
            indices.put(indice.nome(), v);
        }
        return indices;
    }

}
