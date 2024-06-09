function selectEsquema(element) {
    // Remove the selected class from all elements
    var esquemas = document.querySelectorAll('.esquema');
    esquemas.forEach(function(esquema) {
        esquema.classList.remove('selected');
    });

    // Add the selected class to the clicked element
    element.classList.add('selected');
}