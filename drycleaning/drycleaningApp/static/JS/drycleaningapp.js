var slideIndex = 1;
var index = 0;

function plusIndex(n){
    slideIndex += n;
    showSlides(slideIndex);
}
function currentSlide(n){
    slideIndex = n;
    showSlides(slideIndex);
}
showSlides(1);

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) { slideIndex = 1 };
  if (n < 1) { slideIndex = slides.length };

  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
    slides[slideIndex-1].style.display = "block";

  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  dots[slideIndex-1].className += " active";
}

autoSlide();
function autoSlide(){
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");

  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  index++;

  if (index > slides.length) { index = 1 }

  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }

  slides[index-1].style.display = "block";
  dots[index-1].className += " active";
  setTimeout(autoSlide, 8000);
}
