// Este script pertenece al template inventory/createProduct.html
import { ValueInputHidden, inputs } from '../values/valuesFormProductCharascteristic.js';

/* Aquí se recorre los inputs del modal, y si el ID del input coincide con los valores de la llave de los objetos, se encuentra el inputHidden y 
Y se traspasa el valor del input del modal. Esto para evitar hacer un switch que es muy estático */
inputs.forEach( input => {
    input.addEventListener('input', () =>{
        for(  key in ValueInputHidden ){
            if( key == input.id ){
                document.getElementById(ValueInputHidden[key]).value = input.value;
            }
        }
    });
} )
