document.addEventListener("DOMContentLoaded", function() {
    var menuButton = document.getElementById("menu-button");
    var menu = document.getElementById("menu");
    var container = document.querySelector('.container'); // Select the main content container
    var header = document.querySelector('.header'); // Select the header element

    menuButton.addEventListener("click", function() {
        menu.classList.toggle("active");
        container.classList.toggle("blur"); // Toggle the blur class on the container
        header.classList.toggle("blur"); // Toggle the blur class on the header
    });

    // Add an event listener to the document to handle clicks outside the menu
    document.addEventListener("click", function(event) {
        var isClickInsideMenu = menu.contains(event.target);
        var isClickInsideButton = menuButton.contains(event.target);

        // If the click is outside the menu and the button, hide the menu
        if (!isClickInsideMenu && !isClickInsideButton) {
            menu.classList.remove("active");
            container.classList.remove("blur"); // Remove the blur class from the container
            header.classList.remove("blur"); // Remove the blur class from the header
        }   
    });
});
