// Site is fully usable without JavaScript. This only keeps the footer year current.
const year = document.querySelector('#year');
if (year) year.textContent = new Date().getFullYear().toString();
