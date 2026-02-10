class Second:
    def mensaje(self):
        print("second: procesando mensaje()")

        valor = ("hola desde second")
        return valor


def main():
    print("main: iniciando iteraccion")
    second = Second()
    respuesta = second.mensaje()
    print("main: valor retornado ->", respuesta)


if __name__ == "__main__":
    main()