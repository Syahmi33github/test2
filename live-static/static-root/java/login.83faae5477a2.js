const kotak = document.querySelector('.kotak');
const login = document.querySelector('.login');

function ubahWarna (){
    kotak.classList.add('animationkotak');
    login.classList.add('animationlogin');
}

kotak.onclick = ubahWarna;
