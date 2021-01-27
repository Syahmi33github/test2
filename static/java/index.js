const h2kotaktulisancontent1 = document.querySelector('.h2kotaktulisancontent1');
const gambar1content1 = document.querySelector('.gambar1content1');
const gambar2content1 = document.querySelector('.gambar2content1');
const gambar3content1 = document.querySelector('.gambar3content1');
const h2kotaktulisancontent1shadow = document.querySelector('.h2kotaktulisancontent1shadow');

const h1login = document.querySelector('.h1login');
const h2login = document.querySelector('.h2login');


window.addEventListener('scroll', () => {
    let scroll = window.pageYOffset;
    console.log(scroll);

    if (scroll>=300){
        h2kotaktulisancontent1.classList.add('animasih2kotaktulisancontent1');
        gambar1content1.classList.add('animasigambar1content1');
        gambar2content1.classList.add('animasigambar2content1');
        gambar3content1.classList.add('animasigambar3content1');
        h2kotaktulisancontent1shadow.classList.add('animasih2kotaktulisancontent1shadow');
    }
    
    if (scroll>=1400){
        h1login.classList.add('animasih1login');
        h2login.classList.add('animasih1login');
    }
})

