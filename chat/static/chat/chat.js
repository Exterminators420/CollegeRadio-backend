$(document).ready(function(){

	var socket = new WebSocket('ws://localhost:6379/chat/');
	socket.onopen = websocket_connection;
	socket.onmessage = websocket_msj_recibido;

	$('#formulario').submit(function(e){
		e.preventDefault();
		datos = {
			'name' : $('input[name="name"]').val(),
			'massege': $('input[name="texto"]').val()
		}
		socket.send(JSON.stringify(datos));
		$('#formulario')[0].reset();
	});

});

function websocket_conexion_ok(){
	alert('connection established');
}

function websocket_msj_recibido(e){
	datos = JSON.parse(e.data);
	code = '<div class="col s12">'				+
				'<div class="nombre">'				+
					'<h4>'+ datos.name +'</h4>'	+
				'</div>'							+
				'<div class="contenido">'			+
					'<p>'+ datos.message +'</p>'	+
				'</div>'							+
			'</div>';
	$('#conversacion').append(code);
}