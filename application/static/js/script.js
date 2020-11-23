// application/static/js/script.js


// HAMBURGER MENU

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


// SHOW TRANSLATION BUTTON

const showTranslation = document.querySelectorAll('.show-translation-bttn');

if (showTranslation) {

    const showText = () => {
        let sentence = document.querySelectorAll('.hidden');
        for (let i = 0; i < 3; i++) {
            sentence[i].style.display = 'block';
        }
    }

    for (let i = 0; i < showTranslation.length; i++) {  
        showTranslation[i].addEventListener('click', showText);
    } 

}