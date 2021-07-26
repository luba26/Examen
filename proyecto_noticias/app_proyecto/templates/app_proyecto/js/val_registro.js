mail = document.getElementById("mail").mail;
if( !(/\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)/.test(mail)) ) {
}

rut = document.getElementById("rut").rut;
if( rut == null || rut == "" || /^\s+$/.test(rut) ) {

}


nombre = document.getElementById("nombre").nombre;
if( nombre == null || nombre == Number || /^\s+$/.test(nombre) ) {
}

fecha = document.getElementById("fecha").fecha;
if( fecha == null || fecha == "" || /^\s+$/.test(fecha) ) {
}


fono = document.getElementById("fono").fono;
if( fono == null || fono == "" || /^\s+$/.test(fono) ) {
}