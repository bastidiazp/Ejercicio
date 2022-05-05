var nombre = document.getElementById('nombre');
var apellido = document.getElementById('apellido');
var edad = document.getElementById('edad');
var correo = document.getElementById('correo');
var pass = document.getElementById('pass');

var error = document.getElementById('error');
error.style.color = 'red';

function enviarFormulario(){
    console.log('Enviando formulario...');
var mensajesError = [];

if(nombre.value === null || nombre.value === ''){
    mensajesError.push('Ingresa tu nombre');
}
if(apellido.value === null || apellido.value === ''){
    mensajesError.push('Ingresa tu apellido');
}
if(edad.value === null || edad.value === ''){
    mensajesError.push('Ingresa tu edad');
}
if(correo.value === null || correo.value === ''){
    mensajesError.push('Ingresa tu correo electrónico');
}
if(pass.value === null || pass.value === ''){
    mensajesError.push('Ingresa una contraseña');
}

error.innerHTML = mensajesError.join(', '); 
return false;
}




