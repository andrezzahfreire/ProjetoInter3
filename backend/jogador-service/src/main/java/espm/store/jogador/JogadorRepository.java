package espm.store.jogador;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface JogadorRepository extends JpaRepository<JogadorModel, String> {
    // Adicione consultas personalizadas aqui, se necessário
}
