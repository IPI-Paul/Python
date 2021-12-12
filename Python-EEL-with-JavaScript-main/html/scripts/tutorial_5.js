function jsLoad() {
    var nav = document.getElementById('navbar');
    var menu = document.getElementById('menu');
    nav.style.right = '-250px';
    menu.onclick = function() {
        if (nav.style.right == '-250px') {
            nav.style.right = '10px';
        } else {
            nav.style.right = '-250px';
        }
    } 
    nav.onclick = function() {
        nav.style.right = '-250px';
    }
}
