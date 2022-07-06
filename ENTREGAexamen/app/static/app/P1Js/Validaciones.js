let nombre = document.getElementById('nombre');
let apellido = document.getElementById('apellido');
let edad = document.getElementById('edad');
let correo = document.getElementById('correo');
let pass = document.getElementById('pass');

let error = document.getElementById('error');
error.style.color = 'red';

function enviarFormulario() {
    console.log('Enviando formulario...');
    let mensajesError = [];

    if (nombre.value === null || nombre.value === '') {
        mensajesError.push('Ingresa tu nombre');
    }
    if (apellido.value === null || apellido.value === '') {
        mensajesError.push('Ingresa tu apellido');
    }
    if (edad.value === null || edad.value === '') {
        mensajesError.push('Ingresa tu edad');
    }
    if (correo.value === null || correo.value === '') {
        mensajesError.push('Ingresa tu correo electrónico');
    }
    if (pass.value === null || pass.value === '') {
        mensajesError.push('Ingresa una contraseña');
    }

    error.innerHTML = mensajesError.join(', ');
    return false;
}