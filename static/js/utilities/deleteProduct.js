
export const deleteProduct = ( buttonHtml ) => {
        const buttonsCloseDelete = document.querySelectorAll(`.delete-confirm`)


        // Agregar evento y cada botón de confirmación de borrar.
        buttonHtml.addEventListener('click', () => {
            const valueIdProduct = buttonHtml.dataset.idproduct
            const urlDeleteProduct = `/delete/${valueIdProduct}`

            //  Se realiza un fetch a la vista 'delete/<product_id>/' y se envia el id del producto
            buttonsCloseDelete.forEach(buttonConfirmation => {
                buttonConfirmation.addEventListener('click', () => {
                    fetch(urlDeleteProduct)
                        .then(response => response.json())
                        .then(data => {
                            // Redirigir a home.html
                            window.location.href = data.redirect_url
                        })
                        .catch(console.error);
                })

            });

        })
    
}