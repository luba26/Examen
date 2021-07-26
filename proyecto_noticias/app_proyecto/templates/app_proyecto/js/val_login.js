mail = document.getElementById("mail").mail;
if( !(/\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)/.test(mail)) ) {
    alert('[ERROR] datos ingresados no validos');
  return false;
}


clave = document.getElementById("clave").clave;
if( clave == null || nombre == Number || /^\s+$/.test(clave) ) {
    alert('[ERROR] datos ingresados no validos');
    return false;
}