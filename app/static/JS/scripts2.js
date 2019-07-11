const button= document.querySelector('#botao');

function abrirLogin(){
    button.classList.toggle('ativo');
    window.location.pathname = '/login3';

}

button.onclick= abrirLogin;