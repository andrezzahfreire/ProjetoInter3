package espm.store.jogador;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
    
@Repository
public interface IndiceRepository extends JpaRepository<IndiceModel, String> {
    // Adicione consultas personalizadas aqui, se necessário
}
