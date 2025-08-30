function paginaMenu() {
    let cpf = document.getElementById("cpf").value;
    let nome = document.getElementById("nome").value;
    let senha = document.getElementById("senha").value;

    let erros = [];

    if (cpf === '') {
        erros.push("CPF faltando");
    }
    if (nome === '') {
        erros.push("Nome faltando");
    }
    if (senha === '') {
        erros.push("Senha faltando");
    }

    if (erros.length > 0) {
        alert(erros.join('\n'));
    } else {
        localStorage.setItem('senhaUsuario1', senha);
        localStorage.setItem('nomeUsuario1', nome); 
        localStorage.setItem('cpfUsuario1', cpf);

        alert("Tudo certo");
        window.open('telaInicial.html', '_blank');
    }
}
function paginaLogin() {
    window.location.href = 'login.html'
}

function paginaCadastroHomem() {
    window.location.href = 'CadastroHomem.html'
}
function paginaCadastroMulher() {
    window.location.href = 'CadastroMulher.html'
}
function fazerLogin() {
    let senha = document.getElementById("Senha").value;
    let email = document.getElementById("Email").value;

    let erros = [];

    if (senha === '') {
        erros.push("Senha não registrada");
    }
    if (email === '') {
        erros.push("Email não registrado");
    }

    if (erros.length > 0) {
        alert(erros.join('\n'));
    } else {
        localStorage.setItem('senhaUsuario', senha);
        localStorage.setItem('emailUsuario', email);

        alert("Todas as informações registradas");
        window.open('CadastroData.html', '_blank');
    }
}
function mostrarInformações() {
  
    let nomeSalvo = localStorage.getItem('nomeUsuario1'); 
    let cpfSalvo = localStorage.getItem('cpfUsuario1');
    let senhaSalva1 = localStorage.getItem('senhaUsuario1');


    let emailSalvo = localStorage.getItem('emailUsuario');
    let senhaSalvo = localStorage.getItem('senhaUsuario');


    let emailElement = document.getElementById("email");
    emailElement.textContent = emailSalvo || 'Email não encontrado';

    let senhaElement = document.getElementById("senha");
  
    if (senhaSalvo) {
        senhaElement.textContent = senhaSalvo;
    } else if (senhaSalva1) {
   
        senhaElement.textContent = senhaSalva1;
    } else {
        senhaElement.textContent = 'Senha não encontrada';
    } 

    let cpfElement = document.getElementById("cpf");
    cpfElement.textContent = cpfSalvo || 'CPF não encontrado';

    let nomeElement = document.getElementById("nome");
    nomeElement.textContent = nomeSalvo || 'Nome não encontrado';
}
function Voltar() {
    localStorage.removeItem("senhaUsuario");
    localStorage.removeItem("senhaUsuario1");
    window.location.href = "CadastroData.html";
}


function redirenciona(){
    window.location.href="https://github.com/CarlosEdu0808"
}
function redirenciona1(){
    window.location.href="https://github.com/RyanM28S"
}
function redirenciona2(){
    window.location.href="https://github.com/ViniSantosC"
}
function redirenciona3(){
    window.location.href="https://github.com/GuilhermeBuenoDA"
}