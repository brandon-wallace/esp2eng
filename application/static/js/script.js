// application/static/js/script.js


// HAMBURGER MENU TOGGLE

const hamburgerButton = document.querySelector('.hamburger');
const navigation = document.querySelector('nav');

let menuToggle = false;

if (window.innerWidth < 1050) {
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
} else {
    menuToggle = false;
}


// SHOW TRANSLATION BUTTON

const showTranslation = document.querySelectorAll('.show-translation-bttn');

if (showTranslation) {
    const showText = () => {
        let sentence = document.querySelectorAll('.hidden');
        for (let i = 0; i < sentence.length; i++) {
            sentence[i].style.display = 'block';
        }
    }
    for (let i = 0; i < showTranslation.length; i++) {  
        showTranslation[i].addEventListener('click', showText);
    } 
}


// CLOSE FLASH MESSAGES.

const closeMessageButton = document.querySelector('.close');

if (closeMessageButton) {
    closeMessageButton.addEventListener('click', () => {
        document.querySelector('.message').remove();
    });
}
