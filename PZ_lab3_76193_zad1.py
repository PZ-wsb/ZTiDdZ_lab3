import base64

def szyfrowanie(tekst):
    print(f"Wprowadzono tekst: {tekst}")
    tekst_utf8 = tekst.encode("utf-8")
    szyfr_base64 = base64.b64encode(tekst_utf8)
    zaszyfrowane = szyfr_base64.decode("utf-8")
    print(f"Zaszyfrowany tekst: {zaszyfrowane}")

    if (base64.b64decode(zaszyfrowane.encode("utf-8"))==tekst.encode("utf-8")):
        print("Działa odkodowanie")
    else: print("Nie działa odkodowanie")

szyfrowanie("przykladoweszyfrowanie")


