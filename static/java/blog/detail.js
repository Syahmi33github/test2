var x;
x = 1;

const awal              = document.querySelector(".awal");
const judul             = document.querySelector(".judul");

let tinggi_awal = awal.offsetHeight; 
        
const translate             = document.querySelectorAll(".translate");
const translate2            = document.querySelectorAll(".translate2");
const translate2koma1       = document.querySelectorAll(".translate2koma1");
const judullatarbelakang2   = document.querySelector(".judullatarbelakang2");
const fotolatarbelakang     = document.querySelector('.fotolatarbelakang');
const kotaklatarbelakang    = document.querySelector('.kotaklatarbelakang');
const h2latarbelakang       = document.querySelector('.h2latarbelakang');

const kotakcontent1         = document.querySelector('.kotakcontent1');
const kotakcontent1dua      = document.querySelector('.kotakcontent1dua');

const judulcontent2         = document.querySelector('.judulcontent2');
const gambarcontent2        = document.querySelector('.gambarcontent2');
const gambarcontent2dua     = document.querySelector('.gambarcontent2dua');
const kotakcontent2         = document.querySelector('.kotakcontent2');
const h2content2            = document.querySelector('.h2content2');

window.addEventListener('scroll', () => {
    let scroll = window.pageYOffset;
    console.log(scroll);

    judul.style.opacity = -scroll / (tinggi_awal / 1.5) + 1

    translate.forEach(element => {
        let speed = element.dataset.speed;
        element.style.transform = `translateY(${scroll * speed}px)`;
    })

    if (scroll>=950){
        translate2.forEach(element => {
            let speed = element.dataset.speed;
            element.style.transform = `translateY(${scroll * speed - 500}px)`;
        })

        translate2koma1.forEach(element => {
            let speed = element.dataset.speed;
            element.style.transform = `translateY(${scroll * speed + 160}px)`;
        })
    }

    if (scroll>=560 && x<=1){
        judullatarbelakang2.classList.add('animasijudullatarbelakang2');
        fotolatarbelakang.classList.add('animasifotolatarbelakang');
        kotaklatarbelakang.classList.add('animasikotaklatarbelakang');
        h2latarbelakang.classList.add('animasih2latarbelakang');
    }

    if (scroll>=1730){
        kotaklatarbelakang.classList.add('animasikotaklatarbelakang');
        h2latarbelakang.classList.add('animasih2latarbelakang');
    }

    if (scroll>=2335){
        judulcontent2.classList.add('opacityjudulcontent2');
        gambarcontent2.classList.add('kiri');
        gambarcontent2dua.classList.add('kanan');
        kotakcontent2.classList.add('opacitykotakcontent2');
        h2content2.classList.add('animasih2content2');
    }
})

function depanbelakanglatarbelakangAdd(){
    fotolatarbelakang.classList.add('tukarkotakcontent1dua');
    fotolatarbelakang.classList.add('opacity100');
    fotolatarbelakang.classList.remove('animasifotolatarbelakang');
    fotolatarbelakang.classList.remove('opacity75');
    x=2;
            
}

function depanbelakanglatarbelakangRemove(){
    fotolatarbelakang.classList.remove('tukarkotakcontent1dua');
    fotolatarbelakang.classList.add('opacity75');
    fotolatarbelakang.classList.remove('opacity100');
            
}

fotolatarbelakang.onclick = depanbelakanglatarbelakangAdd;
kotaklatarbelakang.onclick = depanbelakanglatarbelakangRemove;

function depanbelakangcontent1Add (){
    kotakcontent1.classList.add('tukarkotakcontent1');
    kotakcontent1dua.classList.add('tukarkotakcontent1dua');
}

function depanbelakangcontent1Remove (){
    kotakcontent1.classList.remove('tukarkotakcontent1');
    kotakcontent1dua.classList.remove('tukarkotakcontent1dua');
}
        
kotakcontent1.onclick = depanbelakangcontent1Remove;
kotakcontent1dua.onclick = depanbelakangcontent1Add;