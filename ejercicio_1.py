class Libro:
    def __init__(self) -> None:
        self.paginas = 30 # Este libro tiene 30 páginas
        self.tapa = "Tapa dura" # Los libros pueden tener tapa dura o blanca, este tiene dura
        self.genero = "Fantasía" # Los libros pertenecen a un género específico
        self.titulo = "Las crónicas de Narnia" # Los libros tienen un título
        self.autor = "C.S. Lewis" # Los libros tienen un autor
        self.idioma = "Inglés" # Los libros están en un idioma
        self.tipo = "Novela" # Los libros pueden ser de muchos tipos como novela, cómic, etc.
    
    # En un libro se puede leer, escribir, abir, cerrar, pero esto no describe al libro en sí y por ello no vamos a desarrollar estas acciones.
    # ¿Cómo implementamos esto en Python? Muy sencillo, nos puede servir para un dataset o una biblioteca, donde se almacenan, pongamos por ejemplo "Los Libros más famosos del siglo XXI"