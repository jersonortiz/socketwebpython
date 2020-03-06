let tab = new Array(9);
for(let aa=0; aa<tab.length;aa++){
	tab[aa]=0;
}
let role = 'x';

window.onload = function(){
	document.getElementById("gamebutton").addEventListener("click",iniciar);

	var socket=null;

	function iniciar(event){

		socket = io.connect('http://localhost:5000/');
		socket.on('connect', function() {

		console.log('Connect');
		});

		socket.on('message', function(msj) {
			console.log(msj);
			console.log('message');
		});

		socket.on('most', function(msj) {
			console.log(msj);
			console.log('msj');
		});

		socket.on('player_move', function(msj) {
			celdasEnable(true);
			console.log('usuario debe seleccionar');
		});

		socket.on('player_wait', function(msj) {
			celdasEnable(false);
			console.log('disable items');
		});

		socket.on('update_board', function(msj) {

			board = msj['data'].split('|');

			let celdas=document.getElementsByName('celda');

			for (var i = celdas.length - 1; i >= 0; i--) {
				if (board[i]==='O'){
					board[i].innerHTML = '<ion-icon name="close-outline"></ion-icon>';
					tab[i]=1;

				} else if(board[i]==='X'){
					board[i].innerHTML = '<ion-icon name="close-outline"></ion-icon>';
					tab[i]=1;
				}
			}

			console.log('actualiza tablero');
		});

		socket.on('define_role', function(msj) {
			role=msj['data'];
			console.log('actualiza rol: '+role);
		});

		socket.on('result', function(msj) {
			switch(msj['data']){

				case 'win':
				break;
				case 'lose':
				break;
				case 'draw':
				break;
			}
			socket.close()
		});



		function movimiento(event){
			console.log("marcar")

			let idele = event.target.id

			let va = idele.split("_");
			let val = va[1];
			console.log(tab);


			if(tab[val]===0){

				socket.emit('player_move', {'data':val});
				let ele = document.getElementById('idele');

				if(role==='X'){
					ele-innerHTML = '<ion-icon name="close-outline"></ion-icon>';
				}	else {
					innerHTML = '<ion-icon name="close-outline"></ion-icon>';
				}
				tab[val]=1;	      
			} 
		}

		celdasEnable(true);

	}


	function celdasEnable(status){
		let celdas=document.getElementsByName('celda');
		for (var i = celdas.length - 1; i >= 0; i--) {
			if(status){
				celdas[i].addEventListener('click',movimiento);
			} else {
				celdas[i].removeEventListener('click',movimiento)
			}		
		}
	}	

}