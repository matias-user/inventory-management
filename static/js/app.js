import { deleteProduct } from './utilities/deleteProduct.js'

document.addEventListener('DOMContentLoaded', function () {
    const deleteButtons = document.querySelectorAll('.borrar');

    deleteButtons.forEach( buttonHtml => deleteProduct(buttonHtml) );

});



