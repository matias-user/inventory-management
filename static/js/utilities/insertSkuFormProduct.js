
const fieldSkuForm = document.getElementById('id_sku');
const paragraph = document.createElement('p');
paragraph.textContent = 'Generar un SKU';
paragraph.classList.add('link-opacity-50-hover');

fieldSkuForm.insertAdjacentElement('afterend', paragraph);
    
