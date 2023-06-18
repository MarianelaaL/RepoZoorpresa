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

function mostrarHoraActual() {
        // Hacer una solicitud a la API World Time
        fetch('http://worldtimeapi.org/api/timezone/America/Santiago')
          .then(response => response.json())
          .then(data => {
            // Obtener la fecha y hora actual de la respuesta de la API
            const fechaHora = new Date(data.datetime);
            // Formatear la fecha y hora
            const hora = fechaHora.getHours().toString().padStart(2, '0');
            const minutos = fechaHora.getMinutes().toString().padStart(2, '0');
            const segundos = fechaHora.getSeconds().toString().padStart(2, '0');
            const dia = fechaHora.toLocaleDateString('es-CL', { weekday: 'long', day: 'numeric' });
            // Mostrar la fecha y hora formateada en el elemento HTML con id="hora"
            document.getElementById('hora').textContent = `${hora}:${minutos}:${segundos} - ${dia}`;
          })
          .catch(error => {
            // Manejar el error si la solicitud falla
            console.error('Error al hacer la solicitud a la API World Time:', error);
          });
      }
    
      // Mostrar la hora actual cuando la página se carga por primera vez
      mostrarHoraActual();
    
      // Actualizar la hora cada segundo
      setInterval(mostrarHoraActual, 500);
    

