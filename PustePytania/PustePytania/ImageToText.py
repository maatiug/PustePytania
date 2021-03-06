from PIL import Image
import pytesseract
import requests
import re

def image_to_text( path ):
    """ [PL] Konwertuje zdjęcie na tekst """
    # Przetworzenie obrazu
    resp = requests.get( path, stream=True )
    img = Image.open( resp.raw )

    # Analiza obrzu
    result = pytesseract.image_to_string( img, lang="pol" )

    # Przetworzenie tekstu
    result = clear_text_with_patterns(result)

    # Zwraca wynik
    return result

def clear_text_with_patterns(text: str) -> str:
    patterns_to_rm = [
        r"\n(.)*(PRAWDA)|\n(.)*(FAŁSZ)",
        r"(  )*",
        r"()",
        r"(Odznacz mój wybór)",
        r"( )*[oO]*( )*[oO]*( )*$",
        r"(\n)*",
        r"(  )*",
    ]

    for pattern in patterns_to_rm:
        text = re.compile(pattern).sub('', text)

    return text
