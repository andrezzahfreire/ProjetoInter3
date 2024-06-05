package espm.store.jogador;

import java.util.List;
import java.util.stream.Collectors;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController     
@RequestMapping("/jogadores")
public class JogadorController {

    @Autowired // permite que o controlador acesse os métodos do serviço JogadorService.
    private JogadorService jogadorService;

    @GetMapping
    public List<JogadorOut> getAllJogadores() {
        return jogadorService.findAll().stream().map(JogadorParser::to).collect(Collectors.toList()); 
    }

    @PostMapping
    public JogadorOut create(@RequestBody(required = true) JogadorIn jogador) { // Alterado o tipo do parâmetro e retorno para Account
        System.out.println(jogador);
        return JogadorParser.to(jogadorService.create(JogadorParser.to(jogador)));
    }

    // Outros métodos de CRUD (atualização e exclusão) podem ser adicionados conforme necessário
}
