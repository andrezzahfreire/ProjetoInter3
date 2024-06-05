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
public class JogadorService {

    @Autowired
    private JogadorRepository jogadorRepository;

    @Autowired
    private IndiceService indiceService;

    public Jogador create(Jogador jogador) {
        /*
        Pessoa pessoa = pessoaRepository.findBySource(idSourcePessoa);
        if (pessoa == null) {
            pessoa = pessoaRepository.create(pessoa);
        }

        Time time = timeRepository.findBySource(idSourceTime);
        if (time == null) {
            time = timeRepository.create(time);
        }

        Contrato contrato = contratoRepository.findByAnoPessoaTimePosicao(ano, pessoa.id(), time.id(), idPosicao);
        if (contrato == null) {
            contrato = contratoRepository.create(contrato);
        }

        for (Indice indice : jogador.indices()) {
            Indice indice = Indice.builder()
                .contrato(contrato)
                .indice(indice)
                .valor(valor)
                .texto(texto)
                .build();
            indiceRepository.create(indice);
        }


        return jogadorRepository.save(new JogadorModel(jogador)).to();
        */

        Jogador salvo = jogadorRepository.save(new JogadorModel(jogador)).to();
        for (Indice indice : jogador.indices()) {
            if (indice.texto() == null && indice.valor() == null) continue;
            indice.jogador(salvo);
            Indice indiceSalvo = indiceService.create(indice);
            salvo.indices().add(indiceSalvo);
        }
        return salvo;
    }

    public void delete(@NonNull String id) {
        jogadorRepository.deleteById(id);
    }

    public List<Jogador> findAll() {
        List<Jogador> l = jogadorRepository.findAll().stream().map(JogadorModel::to).collect(Collectors.toList());
        l.forEach(j -> j.indices(indiceService.findByJogador(j.id())));
        return l;
    }

    public Jogador find(@NonNull String id) {
        Jogador jogador = jogadorRepository.findById(id).map(JogadorModel::to).orElse(null);
        if (jogador == null) return null;
        jogador.indices(indiceService.findByJogador(jogador.id()));
        return jogador;
    }
}
