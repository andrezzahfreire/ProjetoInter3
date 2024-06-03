const apiUrl = 'http://localhost:8080/jogadores';

async function fetchData() {
    try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
            throw new Error('Erro ao buscar dados da API');
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Erro:', error);
        return null;
    }
}

async function renderJogadores() {
    const data = await fetchData();
    if (!data) return;

    const jogadoresDiv = document.getElementById('jogadores');
    data.forEach(jogador => {
        const jogadorDiv = document.createElement('div');
        jogadorDiv.innerHTML = `<h2>${jogador.Jogador}</h2>
                                 <p>Posição: ${jogador.posicao}</p>
                                 <p>Índices:</p>
                                 <ul>
                                    ${jogador.indices.map(indice => `<li>${indice.nome}: ${indice.texto ?? indice.valor}</li>`).join('')}
                                 </ul>`;
        jogadoresDiv.appendChild(jogadorDiv);
    });
}

renderJogadores();
