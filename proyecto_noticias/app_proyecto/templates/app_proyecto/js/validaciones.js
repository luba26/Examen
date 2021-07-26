$(function()
{
	//alert('hola mundo en pandemia');
	let numeros = '1234567890';
	let letras  = 'qwertyuiopasdfghjklñzxcvbnm' +
				'QWERTYUIOPASDFGHJKLÑZXCVBNM' +
				'ÁÉÍÓÚáéíóú ';


	$('.nombre').keypress(function(e)
	{
		let caracter = String.fromCharCode(e.which);
		if(letras.indexOf(caracter) < 0)
		{
			return false;
		}
	})

	$('.email').keypress(function(e)
	{
		let correo='@-.,'+'qwertyuiopasdfghjklñzxcvbnm'+'QWERTYUIOPASDFGHJKLÑZXCVBNM'+'1234567890';
		let caracter = String.fromCharCode(e.which);
		if(correo.indexOf(caracter) < 0)
		{
			return false;
		}
	})
	$('.celular').keypress(function(e)
	{
		let caracter = String.fromCharCode(e.which);
		if(numeros.indexOf(caracter) < 0)
		{
			return false;
		}
	})
	$('.rut').keypress(function(e)
	{
		let caracter = String.fromCharCode(e.which);
		if(numeros.indexOf(caracter) < 0)
		{
			return false;
		}
	})
})	
