function Ayuda()
{
    alert('Eliga cualquiera de los encuentros que se encuentran en al parte inferior, seleccione el equipo que usted considera sera ganador o en otro caso el empate, luego ingrese el monto deseado para apostar y listo! si su resultado gana usted también así de fácil y rápido ');
}

function startTime() {
    var today = new Date();
    var days = ["Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"];
    var d = days[today.getDay()];
    var months = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"];
    var mm = months[today.getMonth()];
    var n = today.getDate();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('txt').innerHTML =
    d + "  " + n + " de " + mm + " - " + h + ":" + m + ":" + s;
    var t = setTimeout(startTime, 500);
}
  function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
}

function Ganador()
{
  var monto;
  monto = prompt('Ingrese monto de apuesta: ');
  if(monto>0 && monto!=null)
  {
    var total = parseInt(monto)*2;
    alert('Felicidades! tu apuesta fue la ganadora, monto del premio: '+ total);
    Ganancia(total);
  }
  else
  {
      alert('Numero ingresado no valido');
  }
}

function Perdedor()
{
  var monto;
  monto = prompt('Ingrese monto de apuesta: ');
  if(monto>0 && monto!=null)
  {
    
    alert('Lamentablemente tu apuesta fue la perdedora, monto del premio: '+ 0);
    var total = parseInt(monto)*-1;
      Ganancia(total);
  }
  else
  {
      alert('Numero ingresado no valido');
  }
}
var acumulado = 0;
function Ganancia(x)
{
    acumulado = acumulado + x;
    document.getElementById('acm').innerHTML = acumulado.valueOf();
}
