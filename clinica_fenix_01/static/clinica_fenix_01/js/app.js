/* aquí irá todo el js

/* Función para evaluar las credenciales ingresadas */
function ValidaCredenciales(usuario, password){
    if (usuario.value = password.value){
        console.log(usuario.value + " ha ingresado al sistema!");
        alert("BIENVENIDO "+ usuario.value);
        location.href="./PagePrivate.html";
    }
    else {
        console.log("Ha habido un intento de ingresar en el sistema con el usuario: " + usuario.value);
        alert("NO TIENES ACCESO");
        location.href="./Registro.html";
    };
}
/* Graficos Js electro */

var speedCanvas = document.getElementById("speedChart");

Chart.defaults.global.defaultFontFamily = "Lato";
Chart.defaults.global.defaultFontSize = 18;

var dataFirst = {
    label: "Car A - Speed (mph)",
    data: [0, 59, 75, 20, 20, 55, 40],
    lineTension: 0,
    fill: false,
    borderColor: 'red'
  };

var dataSecond = {
    label: "Car B - Speed (mph)",
    data: [20, 15, 60, 60, 65, 30, 70],
    lineTension: 0,
    fill: false,
  borderColor: 'blue'
  };

var speedData = {
  labels: ["0s", "10s", "20s", "30s", "40s", "50s", "60s"],
  datasets: [dataFirst, dataSecond]
};

var chartOptions = {
  legend: {
    display: true,
    position: 'top',
    labels: {
      boxWidth: 80,
      fontColor: 'black'
    }
  }
};

var lineChart = new Chart(speedCanvas, {
  type: 'line',
  data: speedData,
  options: chartOptions
});


