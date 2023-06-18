function Resultadoimc() {
  var peso = parseInt(document.getElementById("peso").value);
  var altura = parseInt(document.getElementById("altura").value) / 100; // convierte la altura en metros
  var occi = parseInt(document.getElementById("largo").value) / 100;
  var imc = peso / (altura*occi) ;

  if (imc < 18.5) {
    alert("El IMC de su Mascota es: " + imc.toFixed(2) + ". Está en INFRAPESO. Por favor, acuda a un veterinario.");
  } else if (imc < 25) {
    alert("El IMC de su Mascota es: " + imc.toFixed(2) + ". Está en NORMOPESO.");
  } else if (imc < 30) {
    alert("El IMC de su Mascota es: " + imc.toFixed(2) + ". Está en SOBREPESO.");
  } else {
    alert("El IMC de su Mascota es: " + imc.toFixed(2) + ". Está en OBESIDAD. Por favor, acuda a un veterinario.");
  }

  document.getElementById("resultado").value = imc.toFixed(2);
}
