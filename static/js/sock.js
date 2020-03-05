let tab = new Array(9);
for(let aa=0; aa<tab.length;aa++){
    tab[aa]=0;
}


window.onload = function(){
document.getElementById("gamebutton").addEventListener("click",iniciar);

var socket=null;



function iniciar(event){
	socket = io.connect('http://localhost:5000');
 socket.on('connect', function() {
            console.log('Connect');
        });

  socket.on('message', function(msj) {
  	console.log(msj);
            console.log('message');
        });

    socket.on('most', function(msj) {
  	console.log(msj);
            console.log('message');
        });


	function movimiento(event){
		console.log("marcar")
	  
	    let idele = event.target.id

	    let va = idele.split("_");
	    let val = va[1];
	    console.log(tab);

	    if(tab[val]===0){

	    	socket.emit('message', {'nombre':'pepe'});


	        let ele = document.getElementById(idele);
	        console.log(val);
	        ele.innerHTML = '<ion-icon name="close-outline"></ion-icon>';
	        tab[val]=1;
	        let data = {posicion : val}
	        let heads = new Headers();
	      
	   
	    } 
	}



document.getElementById("block_1").addEventListener("click",movimiento);
document.getElementById("block_2").addEventListener("click",movimiento);
document.getElementById("block_3").addEventListener("click",movimiento);
document.getElementById("block_4").addEventListener("click",movimiento);
document.getElementById("block_5").addEventListener("click",movimiento);
document.getElementById("block_6").addEventListener("click",movimiento);
document.getElementById("block_7").addEventListener("click",movimiento);
document.getElementById("block_8").addEventListener("click",movimiento);
document.getElementById("block_9").addEventListener("click",movimiento);





	

}

}




