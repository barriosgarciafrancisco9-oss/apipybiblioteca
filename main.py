from fastapi import FastAPI, HTTPException
from models import Editorial, Libro

app = FastAPI(title="API Biblioteca", version="1.0")

# 4 Editoriales
ed1 = Editorial(idEd=1, nombre="Addison-Wesley", pais="Estados Unidos")
ed2 = Editorial(idEd=2, nombre="O'Reilly Media", pais="Estados Unidos")
ed3 = Editorial(idEd=3, nombre="Alfaomega", pais="México")
ed4 = Editorial(idEd=4, nombre="Anaya Multimedia", pais="España")

editoriales_db = {ed.idEd: ed for ed in [ed1, ed2, ed3, ed4]}

# 5 Libros
lib1 = Libro(ISBN="978-0132350884", titulo="Clean Code", autor="Robert C. Martin", precio=45.50, editorial=ed1)
lib2 = Libro(ISBN="978-1491957660", titulo="Designing Data-Intensive Applications", autor="Martin Kleppmann", precio=50.00, editorial=ed2)
lib3 = Libro(ISBN="978-6076227282", titulo="Fundamentos de Programación", autor="Luis Joyanes Aguilar", precio=35.00, editorial=ed3)
lib4 = Libro(ISBN="978-8441542389", titulo="Python Crash Course", autor="Eric Matthes", precio=40.20, editorial=ed4)
lib5 = Libro(ISBN="978-0131103627", titulo="The C Programming Language", autor="Brian Kernighan", precio=38.90, editorial=ed1)

libros_db = {lib.ISBN: lib for lib in [lib1, lib2, lib3, lib4, lib5]}

# Método GET 1: Consultar Libro
@app.get("/libros/{isbn}")
def obtener_libro(isbn: str):
    if isbn not in libros_db:
        raise HTTPException(status_code=404, detail=f"El libro con ISBN '{isbn}' no fue encontrado.")
    lib = libros_db[isbn]
    return {
        "ISBN": lib.ISBN,
        "titulo": lib.titulo,
        "autor": lib.autor,
        "precio": lib.precio,
        "editorial": {
            "idEd": lib.editorial.idEd,
            "nombre": lib.editorial.nombre,
            "pais": lib.editorial.pais
        }
    }

# Método GET 2: Consultar Editorial
@app.get("/editoriales/{id_ed}")
def obtener_editorial(id_ed: int):
    if id_ed not in editoriales_db:
        raise HTTPException(status_code=404, detail=f"La editorial con ID {id_ed} no fue encontrada.")
    ed = editoriales_db[id_ed]
    return {
        "idEd": ed.idEd,
        "nombre": ed.nombre,
        "pais": ed.pais
    }