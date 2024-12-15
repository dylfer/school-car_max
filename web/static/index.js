document.addEventListener("DOMContentLoaded", function () {
  const elements = document.querySelectorAll(".slide-in-left, .slide-in-right");

  function isInView(element) {
    const rect = element.getBoundingClientRect();
    return (
      rect.top <
        (window.innerHeight || document.documentElement.clientHeight) &&
      rect.bottom > 0 &&
      rect.left < (window.innerWidth || document.documentElement.clientWidth) &&
      rect.right > 0
    );
  }

  function checkElements() {
    elements.forEach((element) => {
      if (isInView(element)) {
        element.classList.add("active");
      }
    });
  }

  window.addEventListener("scroll", checkElements);
  window.addEventListener("resize", checkElements);
  checkElements(); // Initial check
});
