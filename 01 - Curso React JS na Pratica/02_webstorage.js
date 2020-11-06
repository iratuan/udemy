// // Webstorage
// localStorage.setItem('nome', 'iratuan junior');
// localStorage.setItem('email', 'iratuan@gmail.com');

// // Removendo itens
localStorage.removeItem('nome');
// localStorage.sobrenome = 'nobre';
// localStorage.nome = 'iratuan';

var nome = '';

if(typeof localStorage.nome == 'undefined'){
    localStorage.nome = prompt('Digite seu nome:');
}

nome = localStorage.nome;

document.getElementById('nome').innerHTML = nome;