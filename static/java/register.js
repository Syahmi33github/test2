const labeltag = document.getElementsByClassName('labeltag');
const titlepage = document.querySelector('.titlepage');
const nightmode = document.querySelector('.nightmode');

function ubahWarna (){
    for(let i = 0; i < labeltag.length; i++)
    labeltag[i].classList.toggle('tulisanhitam');
    titlepage.classList.toggle('tulisanabu');
    nightmode.classList.toggle('logobulansabit');
}

nightmode.onclick = ubahWarna;