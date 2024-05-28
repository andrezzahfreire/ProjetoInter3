package espm.store.jogador;

public final class JogadorParser {
    
    public static Jogador to(JogadorIn in) {
        return null == in ? null : Jogador.builder()
            .jogador(in.jogador())
            .nacionalidade(in.nacionalidade())
            .posicao(in.posicao())
            .equipe(in.equipe())
            .idade(in.idade())
            .nascimento(in.nascimento())
            .indices(IndiceParser.to(in.indices()))
            .build();
    }

    public static JogadorOut to(Jogador account) {
        return null == account ? null : new JogadorOut(
            account.id(),
            account.jogador(),
            account.nacionalidade(),
            account.posicao(),
            account.equipe(),
            account.idade(),
            account.nascimento(),
            IndiceParser.to(account.indices())
        );
    }
}
