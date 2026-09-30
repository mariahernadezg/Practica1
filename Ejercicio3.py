def process_text(text: str = "This is a default text with Python and amazing words.",
                  words_replace: list[str] = ["Python", "amazing"] ) -> tuple[str, int]:
    """
        Busca en la cadena de texto las palabras de la lista y las remplaza por asteriscos

        Par:
             str text: cadena de texto a evaluar, valor predeterminado por defecto
             lista words_replace: lista de palabras a buscar y reemplazar
        Devuelve:
             string processed_words: la cadena de texto en minúsculas con las palanras coincidentes reemplazadas por asteriscos
             int count: el número de palabras que han sido reemplazadas
    """
    text = text.lower()
    cleaned_text = text.strip().lower()

    rem_lower = []
    for w in words_replace:
        rem_lower.append(w.lower())

    
    words = cleaned_text.split()
    processed_words = []
    count = 0

    for w in words:
        if w in rem_lower:
            processed_words.append("*" * len(w))
            count += 1
        else:
            processed_words.append(w)

    processed_text = " ".join(processed_words)

    return processed_text, count

