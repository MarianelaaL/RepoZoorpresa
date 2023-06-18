$(function(){
    $("#datos").validate({
        rules:{
            rut:{
                required:true
            },

            nom:{
                required:true
            },

            apellidos:{
                required:true
            },

            email:{
                required:true,
                email:true
            },

            fono:{
                required: true
            },
            lista:{
                required: true
            }
        },

        messages:{
            rut:{
                required: 'Ingrese su rut',
            },

            nom:{
                required: 'Ingrese su nombre',
                minlength: 'Caracteres insuficientes (3)'
            },

            apellidos:{
                required: 'Ingrese su apellido',
                minlength: 'Caracteres insuficientes (3)'
            },

            email:{
                required: 'Ingrese su correo',
                email: 'Formato de correo no valido'
            },

            fono:{
                required: 'Ingrese numero de telefono',
                minlength: 'Digitos insuficientes (9)'
            },
            lista:{
                required: 'Requiere elegir algun elemento de la lista'
            }
        },
        

    })
});


/*const inputRut = document.getElementById("rut");

function validarRut() {

    // Eliminar puntos y guiones del RUT y convertirlo a un número entero
    const rut = inputRut.value.replace(/\./g, '').replace('-', '');
    const numero = parseInt(rut.slice(0, -1));
    const digitoVerificador = rut.slice(-1).toUpperCase();
  
    // Calcular el dígito verificador esperado
    let suma = 0;
    let multiplicador = 2;
    while (numero > 0) {
      suma += multiplicador * (numero % 10);
      numero = Math.floor(numero / 10);
      multiplicador++;
      if (multiplicador > 7) {
        multiplicador = 2;
      }
    }
    const digitoEsperado = 11 - (suma % 11);

    return digitoEsperado;
};

function escritoRutValido(){
    input.onblur = function(){
        if (validarRut()==10 || validarRut()==11 || validarRut()<10){
            alert('Rut Valido');
        }
        else{
            alert('Rut invalido');
        }
    }  
}
*/

window.onload = function() {
    const inicio = document.getElementById('pethome');
    const productos = document.getElementById('prod');
    const sobreNosotros = document.getElementById('sobren');
    const formulario = document.getElementById('form');
  
    inicio.addEventListener('mouseover', function() {
      this.style.fontSize = '30px';
      this.style.color = 'red'
    });
  
    inicio.addEventListener('mouseout', function() {
      this.style.fontSize = '20px';
    });

    productos.addEventListener('mouseover', function() {
        this.style.fontSize = '30px';
        this.style.color = 'red'
      });
    
    productos.addEventListener('mouseout', function() {
        this.style.fontSize = '20px';
      });
    sobreNosotros.addEventListener('mouseover', function() {
        this.style.fontSize = '30px';
        this.style.color = 'red'
      });
    
    sobreNosotros.addEventListener('mouseout', function() {
        this.style.fontSize = '20px';
      });

    formulario.addEventListener('mouseover', function() {
        this.style.fontSize = '30px';
        this.style.color = 'red'
      });
    
    formulario.addEventListener('mouseout', function() {
        this.style.fontSize = '20px';
      });
    
  }
  

