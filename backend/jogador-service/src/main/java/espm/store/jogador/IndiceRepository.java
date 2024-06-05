package espm.store.jogador;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import java.util.List;

    
@Repository
public interface IndiceRepository extends JpaRepository<IndiceModel, String> {

    List<IndiceModel> findByJogador(String jogador);

}
