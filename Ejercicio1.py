def is_integer(text: str) ->bool:
    """
    Devuelve True si la cadena es un numero entero, sino, devuelve False.

    Par:
        string text: cadena a evaluar
    Devuelve:
        bool: True si es un numero entero, False si no lo es
    """
    try:
        int(text)
        return True
    except ValueError:
        return False

def seconds_to_dhms(total_seconds: int) ->str:
    """
    Convierte los segundos a días, horas, minutos y segundos

    Par:
        int total_seconds: segundos
    Devuelve:
        str: días, horas, minutos y segundos equivalentes a los segundos introducidos
    """
    if total_seconds>=0:
        dias = total_seconds//86400
        total_seconds %= 86400
        horas = total_seconds//3600
        total_seconds %= 3600
        minutos = total_seconds//60
        segundos = total_seconds%60

        return dias, horas, minutos, segundos
    else:
        print("Introduzca un entero no negativo")

def main():
    while True:
        text = input("Introduzca los segundos: ")
        if is_integer(text):
            total_seconds = int(text)
            if total_seconds >= 0:
                break
        print("Entrada no válida. Introduzca un entero no negativo.")

    days, hours, minutes, seconds = seconds_to_dhms(total_seconds)
    print(f"{total_seconds} segundos son {days} d, {hours} h, {minutes} min y {seconds} s.")

if __name__ == "__main__":
    main()