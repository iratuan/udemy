function acao(){
    console.log("Executando");
}

// Executa uma ação no intervalo de milisgundos
//setInterval(acao, 1000);


// Nesse caso, ele executa uma vez e depois para.
//setTimeout(acao, 3000);


// Atribuindo o setInterval a uma variavel e controlando sua execução
var timer = setInterval(acao, 1000);
// Interrompe o setInterval
clearInterval(timer);