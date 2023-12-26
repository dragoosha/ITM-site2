const slider = document.querySelector('.image-container');
const sliderImages = document.querySelectorAll('.slider__img');
const sliderLine = document.querySelector('.slider__line');
const imageContainer = document.querySelector('.image-container');
const sliderBtnPrev = document.querySelector('.slider__btn-prev');
const sliderBtnNext = document.querySelector('.slider__btn-next');

let sliderCount = 0;
let sliderWidth = slider.offsetWidth;

sliderBtnNext.addEventListener('click', nextSlide);
sliderBtnPrev.addEventListener('click', prevSlide);


function nextSlide() {
    sliderCount++;

    if (sliderCount >= sliderImages.length - 5) {
        sliderCount = 0;
    }

    rollSlider();
}

function prevSlide() {
    sliderCount--;

    if(sliderCount >= sliderImages.length - 5) {
        sliderCount = 0;
    }

    rollSlider();
}

function rollSlider () {
    sliderLine.style.transform = `translateX(${-sliderCount * sliderWidth}px`;
}

setInterval(() => {
    nextSlide()
}, 3000);
