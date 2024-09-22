const select = document.querySelector('select');

const getProductsOrderedByCharacteristic = ( characteristic ) => {
    const urlView = `/home/${characteristic}/`;

    fetch(urlView, {
        method:'GET'
    })
    .then( response => {
        window.location.href = urlView

    } );
}

select.addEventListener('change',() => {
   
    getProductsOrderedByCharacteristic(select.value)
    
});
