from flask import Flask, jsonify, request
from data import books
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return jsonify(books)

@app.route('/ingresar', methods=['POST'])
# @cross_origin()
def ingresar():
    new_book = {
        "name": request.json['name'],
        "author": request.json['author'],
        "year": request.json['year']
    }
    books.append(new_book)
    return jsonify({"message": "Libro agregado exitosamente", "books": books})

@app.route('/retirar<string:name>', methods=['DELETE'])
def retirar(name):
    libro_eliminar = [libro for libro in books if libro['name'].lower() == name.lower()]
    if len(libro_eliminar) > 0:
        books.remove(libro_eliminar[0])
        return jsonify({"message": "Libro eliminado", "books": books})
    return jsonify({"message": "Libro no encontrado"})

@app.route('/buscar/<string:name>')
def buscar(name):
    libros = [libro for libro in books if libro['name'].lower() == name.lower()]
    if len(libros) > 0:
        return jsonify({"book": libros[0]})
    else:
        return jsonify({"message": "Libro no encontrado"})

@app.route('/actualizar/<string:name>', methods=['PUT'])
def actualizar(name):
    libro_enontrado = [libro for libro in books if libro['name'].lower() == name.lower()]
    print(libro_enontrado)
    if len(libro_enontrado) > 0:
        libro_enontrado[0]['name'] = request.json['name']
        libro_enontrado[0]['author'] = request.json['author']
        libro_enontrado[0]['year'] = request.json['year']
        return jsonify({"message": "Libro actualizado", "book": libro_enontrado[0]})
    return jsonify({"message": "Libro no encontrado"}), 404


# Correr el servidor si se ejecuta este archivo
if __name__ == '__main__':
    app.run(debug=True, port=4000)