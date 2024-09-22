import { deleteProduct } from './utilities/modal.js'

document.addEventListener('DOMContentLoaded', function () {
    const deleteButtons = document.querySelectorAll('.borrar');

    deleteButtons.forEach( buttonHtml => deleteProduct(buttonHtml) );

});



