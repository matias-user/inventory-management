// const buttonCharacteristic = document.querySelector('button[data-bs-toggle=modal]');
import { inputsHidden, inputs } from '../values/valuesFormProductCharascteristic.js';

inputs.forEach( (input, idx) => {
    console.log(inputsHidden[idx].value);
    
    input.value = inputsHidden[idx].value
} );