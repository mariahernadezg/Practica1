def is_leap_year(year: int) -> bool:
    """
    Devuelve True si el año es bisiesto y False si no lo es

    Par:
        int year: año a evaluar
    Devuelve:
        bool: True si es bisiesto y False si no
    """
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def leap_year_between(start: int, end: int) -> list[int]:
    """
    Devuelve la lista de los años bisiestos entre start y end

    Par:
        int start: año de inicio de la lista
        int end: año de fin de la lista
    Devuelve:
        list[int]: lista de los años bisiestos entre start y end
    """
    bis = []

    for year in range(start, end+1):

        if is_leap_year(year):
            bis.append(year)
    return bis

def explain_leap_year(year: int) -> str:
    """
        Indica si el año es bisiesto y por qué
        Par:
            int year: año a evaluar
        Devuelve:
            str: cadena con la expliación de por qué es o no año bisiesto
    """
    if year % 400 == 0:
        return f"{year} es bisiesto: es divisible entre 400."
    elif year % 100 == 0:
        return f"{year} no es bisiesto: es divisible entre 100 pero no entre 400."
    elif year % 4 == 0:
        return f"{year} es bisiesto: es divisible entre 4 y no entre 100."
    else:
        return f"{year} no es bisiesto: no es divisible entre 4."


def main():
    while True:
        year = int(input("Año: "))
        if year < 1582:
            print("El calendario gregoriano se estableció en 1582")
        else:
            print(explain_leap_year(year))
            break

    print("Ejemplo de uso de leap_years_between entre 1896 y 1912")
    print(leap_year_between(1896, 1912))

if __name__ == "__main__":
    main()
    
          
      