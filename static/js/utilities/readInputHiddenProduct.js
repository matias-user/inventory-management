// Este script pertenece al template inventory/createProduct.html
const inputHeight = document.getElementById('input_height');
const inputWeight = document.getElementById('input_weight');
const inputColor = document.getElementById('input_color');
const inputMaterialType = document.getElementById('input_material_type');

const inputs = [ inputHeight, inputWeight, inputColor, inputMaterialType ];

const inputHeightHidden = document.getElementById('id_height');
const inputWeightHidden = document.getElementById('id_weight');
const inputColorHidden = document.getElementById('id_color');
const inputMaterialTypeHidden = document.getElementById('id_material_type');

const inputsHidden = [inputColorHidden, inputHeightHidden, inputWeightHidden, inputMaterialTypeHidden];

const ValueInputHidden = {
    [inputHeight.id]: inputHeightHidden.id,
    [inputWeight.id]: inputWeightHidden.id,
    [inputColor.id]: inputColorHidden.id,
    [inputMaterialType.id]: inputMaterialTypeHidden.id,
}

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
