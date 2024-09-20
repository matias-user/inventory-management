

document.addEventListener('DOMContentLoaded', function () {
    const deleteButtons = document.querySelectorAll('.borrar');

    // Redirigir a home, cuando se borra un producto de la lista principal en home.html

    deleteButtons.forEach(buttonHtml => {

        buttonHtml.addEventListener('click', () => {
            const valueIdProduct = buttonHtml.dataset.idproduct
            const buttonsCloseDelete = document.querySelectorAll(`.delete-confirm`)

            const urlBorrar = `/delete/${valueIdProduct}`

            buttonsCloseDelete.forEach(buttonConfirmation => {
                buttonConfirmation.addEventListener('click', () => {
                    fetch(urlBorrar)
                        .then(response => response.json())
                        .then(data => {
                            window.location.href = data.redirect_url
                        })
                        .catch(console.error);
                })

            });

        })
    });

});



