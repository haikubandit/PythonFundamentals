def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    capitalized = []
    words = phrase.split()
    for word in words:
        word = word.lower().capitalize()
        capitalized.append(word)

    return " ".join(capitalized)