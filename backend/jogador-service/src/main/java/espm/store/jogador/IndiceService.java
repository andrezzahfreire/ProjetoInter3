package espm.store.jogador;

import java.util.List;
import java.util.stream.Collectors;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.lang.NonNull;
import org.springframework.stereotype.Service;

/* 
 * Aqui e a camada de regra de negocio.
 */
@Service
public class IndiceService {

    @Autowired
    private IndiceRepository indiceRepository;

    public Indice create(Indice i) {
        return indiceRepository.save(new IndiceModel(i)).to();
    }

    public void delete(@NonNull String id) {
        indiceRepository.deleteById(id);
    }

    public List<Indice> findByJogador(@NonNull String id) {
        return indiceRepository.findByJogador(id).stream()
            .map(IndiceModel::to)
            .collect(Collectors.toList());
    }
}
