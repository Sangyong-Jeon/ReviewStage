const slidesContainer = document.querySelector('.slides');
const slides = document.querySelectorAll('.slides li');
const slideCount = slides.length;
const slideWidth = 300;
const slideMargin = 30;
const prevBtn = document.querySelector('.prev');
const nextBtn = document.querySelector('.next');
let currentIdx = 0;

makeClone();
addEventListeners();

function makeClone() {
    for (let i = 0; i < slideCount; i++) {
        cloneSlide(slides[i]);
    }

    for (let i = slideCount - 1; i >= 0; i--) {
        cloneSlide(slides[i], true);
    }
    updateWidth();
    setInitialPos();
    addAnimation();
}

function cloneSlide(slide, isPrepend = false) {
    const cloneSlide = slide.cloneNode(true);
    cloneSlide.classList.add('clone');
    if (isPrepend) {
        slidesContainer.prepend(cloneSlide);
    } else {
        slidesContainer.appendChild(cloneSlide);
    }
}

function updateWidth() {
    const newSlideCount = document.querySelectorAll('.slides li').length;
    slidesContainer.style.width = (slideWidth + slideMargin) * newSlideCount - slideMargin + 'px';
}

function setInitialPos() {
    slidesContainer.style.transform = `translateX(${-((slideWidth + slideMargin) * slideCount)}px)`;
}

function addAnimation() {
    setTimeout(() => {
        slidesContainer.classList.add('animated');
    }, 100);
}

function addEventListeners() {
    nextBtn.addEventListener('click', () => moveSlide(currentIdx + 1));
    prevBtn.addEventListener('click', () => moveSlide(currentIdx - 1));
}

function moveSlide(num) {
    slidesContainer.style.left = -num * (slideWidth + slideMargin) + 'px';
    currentIdx = num;

    if (currentIdx === slideCount || currentIdx === -slideCount) {
        setTimeout(() => {
            slidesContainer.classList.remove('animated');
            slidesContainer.style.left = '0px';
            currentIdx = 0;
        }, 500);
        setTimeout(addAnimation, 600);
    }
}