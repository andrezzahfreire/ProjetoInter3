window.onload =async function() {
    let Jidade = document.getElementById("idade")
    let Jnacionalidade = document.getElementById("nacionalidade")
    let Jclube = document.getElementById("clube")
    let Jposicao = document.getElementById("posicao")
    let gEsperados = document.getElementById("gE")
    let gNorEsperados = document.getElementById("gNE")
    let gAssEsperados = document.getElementById("gAE")
    let Jogador = localStorage.getItem("jogad")
    

    let JogadorAtual;

        await fetch('../web_scraping/dados_jogadores.csv')
        .then(response => response.text())
        .then(csv => {
          const json = Papa.parse(csv, { header: true, dynamicTyping: true, preview: 752 });
          console.log(json)
    json.data.forEach((item) => {
        if(Jogador == item.jogador){
            JogadorAtual = item
        }
        
        })
        console.log(JogadorAtual)
        });
        Jidade.innerHTML =`<p>${JogadorAtual["idade"]}</p>`
        Jnacionalidade.innerHTML=`<p>${JogadorAtual["nacionalidade"]}</p>`
        Jclube.innerHTML=`<p>${JogadorAtual["equipe"]}</p>`
        Jposicao.innerHTML=`<p>${JogadorAtual["posicao"]}</p>`
        let indice = JogadorAtual["indices"].split(",")
        gEsperados.innerHTML=`<p>${parseFloat(indice[12].slice(7))}</p>`
        gNorEsperados.innerHTML=`<p>${parseInt(indice[13].slice(9))}</p>`
        gAssEsperados.innerHTML=`<p>${parseInt(indice[14].slice(8))}</p>`
        let cAmarelos = parseInt(indice[10].slice(10,indice[10].indexOf(".")))
        let cVermelho = parseInt(indice[11].slice(9,indice[11].indexOf(".")))
        let gols =  parseInt(indice[4].slice(9,indice[4].indexOf(".")))/20
        let assistencias =  parseInt(indice[5].slice(11,indice[5].indexOf(".")))/11
        let tmpJogo  =  parseInt(indice[3].slice(8,indice[3].indexOf(".")))/110
        let passesP =  parseInt(indice[17].slice(9,indice[17].indexOf(".")))/231
        

    var ctx1 = document.getElementById('pieChart').getContext('2d');
    var pieChart = new Chart(ctx1, {
        type: 'pie',
        data: {
            labels: cAmarelos+cVermelho == 0 ?["jogador sem cartões"]:['Cartões Amarelos', 'Cartões Vermelhos'],
            datasets: [{
                data: cAmarelos+cVermelho == 0 ?[1]:[cAmarelos, cVermelho],
                backgroundColor:cAmarelos+cVermelho == 0 ?["#eeeeee"]:['#dac80f', '#9b111e']
            }]
        },
        options: {
            responsive: true
        }
    });

    var ctx2 = document.getElementById('lineChart').getContext('2d');
    var lineChart = new Chart(ctx2, {
        type: 'bar',
        data: {
            labels: ["total de gols"],
            datasets: [{
                label: JogadorAtual["jogador"],
                data: [gols*20],
                backgroundColor: '#ff6384'
            }, {
                label: 'Média de gols desta posição',
                data: JogadorAtual["posicao"] == "AT"?[3.2]:JogadorAtual["posicao"] == "AT,LT"?[2.1]:JogadorAtual["posicao"] == "AT,ZG"?[0.5]:JogadorAtual["posicao"] == "G"?[0]:JogadorAtual["posicao"] == "LT"?[0.8]:JogadorAtual["posicao"] == "LT,AT"?[1.6]:JogadorAtual["posicao"] == "LT,ZG"?[0.7]:JogadorAtual["posicao"] == "ZG"?[0.4]:JogadorAtual["posicao"] == "ZG,AT"?[0.1]:JogadorAtual["posicao"] == "ZG,LT"?[0.45]:[0],
                backgroundColor: '#36a2eb'
            }]
        },
        options: {
            responsive: true
        }
    });

    var ctx3 = document.getElementById('radarChart').getContext('2d');
    var radarChart = new Chart(ctx3, {
        type: 'radar',
        data: {
            labels: ['Gols', 'Assistências', 'Tempo de jogo', 'Passes progressivos'],
            datasets: [{
                label: 'desempenho',
                data: [gols, assistencias , tmpJogo , passesP  ],
                borderColor: '#ff6384',
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                fill: true

            }]
        },
        options: {
            responsive: true,
            scales: {
                r: {
                    angleLines: {
                        display: false
                    },
                    suggestedMin: 0,
                    suggestedMax: 1
                }
            }
        }
    });

    var ctx4 = document.getElementById('barChart').getContext('2d');
    var barChart = new Chart(ctx4, {
        type: 'bar',
        data: {
            labels: ["total de gols"],
            datasets: [{
                label: JogadorAtual["jogador"],
                data: [gols*20],
                backgroundColor: '#ff6384'
            }, {
                label: 'Média do campeonato',
                data: [1.22],
                backgroundColor: '#36a2eb'
            }]
        },
        options: {
            responsive: true
        }
    });
    localStorage.removeItem("jogad")
};
