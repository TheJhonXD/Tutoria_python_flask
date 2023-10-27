let btn_ingresar = document.getElementById('btn-ingresar');
let btn_actualizar = document.getElementById('btn-actualizar');
let btn_buscar = document.getElementById('btn-buscar');
let btn_retirar = document.getElementById('btn-retirar');

// METODO Post
btn_ingresar.addEventListener('click', async () => {
    let data = {
        "name": document.getElementById('new_name').value,
        "author": document.getElementById('new_author').value,
        "year": document.getElementById('new_year').value
    }

    try {
        const res = await fetch(`http://127.0.0.1:4000/ingresar`, {
            method: 'POST',
            cors: 'cors',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });

        if (!res.ok) {
          throw new Error(`Error al realizar la solicitud: ${res.status} - ${res.statusText}`);
        }
        
        const datos = await res.json();
        if (res.ok){
            alert("Libro ingresado correctamente");
        }
        console.log(datos);
      } catch (error) {
        console.error(`Hubo un error: ${error}`);
      }
});


// METODO PUT
btn_actualizar.addEventListener('click', async () => {
  let buscado = document.getElementById('book-name').value;
    let data = {
        "name": document.getElementById('update-name').value,
        "author": document.getElementById('update-author').value,
        "year": document.getElementById('update-year').value
    }
  
    try {
        const res = await fetch(`http://127.0.0.1:4000/actualizar/${buscado}`, {
            method: 'PUT',
            cors: 'cors',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });

        if (!res.ok) {
          throw new Error(`Error al realizar la solicitud: ${res.status} - ${res.statusText}`);
        }
        
        const datos = await res.json();
        alert("Libro actualizado");
        console.log(datos);
      } catch (error) {
        console.error(`Hubo un error: ${error}`);
      }
});


// METODO GET
btn_buscar.addEventListener('click', async () => {
  const buscado = document.getElementById('libro-buscado').value;
  try {
    const res = await fetch(`http://127.0.0.1:4000/buscar/${buscado}`);

    if (!res.ok) {
      throw new Error(`Error al realizar la solicitud: ${res.status} - ${res.statusText}`);
    }
    
    const datos = await res.json();
    console.log(datos);
  } catch (error) {
    console.error(`Hubo un error: ${error}`);
  }
});

// METODO DELETE
btn_retirar.addEventListener('click', async () => {
  const retirar = document.getElementById('libro-retirar').value;
  try {
    const res = await fetch(`http://127.0.0.1:4000/retirar/${retirar}`, {
      method: 'DELETE'
    });

    if (!res.ok) {
      throw new Error(`Error al realizar la solicitud: ${res.status} - ${res.statusText}`);
    }
    
    const datos = await res.json();
    console.log(datos);
  } catch (error) {
    console.error(`Hubo un error: ${error}`);
  }
});

