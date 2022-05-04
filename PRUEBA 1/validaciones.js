var nombre = document.getElementById('nombre');
var apellido = document.getElementById('apellido');
var edad = document.getElementById('edad');
var pais = document.getElementById('paises');
var region = document.getElementById('regiones');
var flores = document.getElementById('flores');
var interes = document.getElementById('interes');
var correo = document.getElementById('correo');
var pass = document.getElementById('pass');

var error = document.getElementById('error');
error.style.color = 'red';

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
if(pais.value === null || pais.value === ''){
    mensajesError.push('Selecciona tu país');
}
if(region.value === null || region.value === ''){
    mensajesError.push('Selecciona tu región');
}
if(flores.value === null || flores.value === ''){
    mensajesError.push('Selecciona tus flores preferidas');
}
if(interes.value === null || interes.value === ''){
    mensajesError.push('Selecciona tu área');
}
if(correo.value === null || correo.value === ''){
    mensajesError.push('Ingresa tu correo electrónico');
}
if(pass.value === null || pass.value === ''){
    mensajesError.push('Ingresa tu una contraseña');
}

error.innerHTML = mensajesError.join(', ');






