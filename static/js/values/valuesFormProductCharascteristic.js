const inputHeight = document.getElementById('input_height');
const inputWidth = document.getElementById('input_width');
const inputColor = document.getElementById('input_color');
const inputMaterialType = document.getElementById('input_material_type');

const inputs = [ inputHeight, inputWidth, inputColor, inputMaterialType ];

const inputHeightHidden = document.getElementById('id_height');
const inputWidthHidden = document.getElementById('id_width');
const inputColorHidden = document.getElementById('id_color');
const inputMaterialTypeHidden = document.getElementById('id_material_type');

const inputsHidden = [ inputHeightHidden, inputWidthHidden, inputColorHidden,inputMaterialTypeHidden];

const ValueInputHidden = {
    [inputHeight.id]: inputHeightHidden.id,
    [inputWidth.id]: inputWidthHidden.id,
    [inputColor.id]: inputColorHidden.id,
    [inputMaterialType.id]: inputMaterialTypeHidden.id,
}


export { inputs, inputsHidden, ValueInputHidden };