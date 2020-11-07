// application/static/js/script.js

const hamburgerButton = document.querySelector('.hamburger');
const navigation = document.querySelector('nav');

let menuToggle = false;

if (window.innerWidth < 750) {
    hamburgerButton.addEventListener('click', () => {
        menuToggle = menuToggle === false ? true : false;
        if (menuToggle) {
          menuToggle = true;
          navigation.style.display = 'flex';
        } else {
          menuToggle = false;
          navigation.style.display = 'none';
        }
    });
}


const showTranslation = document.querySelectorAll('.show-translation-bttn');


/*
if (showTranslation) {

    console.log(`Button is available`);

    const showText = () => {
        let sentences = [...document.querySelectorAll('.hidden')]
        sentences.forEach(elem => elem.style.display = 'block');
    }

    showTranslation.addEventListener('click', showText);

}
*/

const whichButton = (event) => {
    const parentN = event.target.parentNode;
    console.log(parentN);
}

showTranslation.forEach(bttn => {
    bttn.addEventListener('click', whichButton)
});

//const tileImage = document.querySelectorAll('.tile-img');
//
//
//const openModal = (event) => {
//    const modalImage = event.target.alt;
//    document.querySelector('.'+modalImage).style.display = 'flex';
//}
//
//
//tileImage.forEach(tile => {
//    tile.addEventListener('click', openModal);
//});
//
//
//const closeModal = () => {
//    const modals = document.querySelectorAll('.modal');
//    for (let i = 0; i < modals.length; i++) {
//        modals[i].style.display = 'none';
//    }
//}
