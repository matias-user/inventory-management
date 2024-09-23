// Este script pertenece al template inventory/createProduct.html
const inputHeight = document.getElementById('input_height');
const inputWidth = document.getElementById('input_width');
const inputColor = document.getElementById('input_color');
const inputMaterialType = document.getElementById('input_material_type');

const inputs = [ inputHeight, inputWidth, inputColor, inputMaterialType ];

const inputHeightHidden = document.getElementById('id_height');
const inputWidthHidden = document.getElementById('id_width');
const inputColorHidden = document.getElementById('id_color');
const inputMaterialTypeHidden = document.getElementById('id_material_type');

const inputsHidden = [inputColorHidden, inputHeightHidden, inputWidthHidden, inputMaterialTypeHidden];

const ValueInputHidden = {
    [inputHeight.id]: inputHeightHidden.id,
    [inputWidth.id]: inputWidthHidden.id,
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
