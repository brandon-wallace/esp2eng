// application/static/js/script.js

const hamburgerButton = document.querySelector('.hamburger');
const navigation = document.querySelector('nav');

let menuToggle = false;

//if (window.innerWidth < 750) {
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
//}


const showTranslation = document.querySelector('.show-translation-bttn');

if (showTranslation) {

    console.log(`Button is available`);

    const showText = () => {
        let sentences = [...document.querySelectorAll('.hidden')]
        sentences.forEach(elem => elem.style.display = 'block');
    }

    showTranslation.addEventListener('click', showText);

}

