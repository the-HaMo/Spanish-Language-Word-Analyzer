import re

def silabear(cadena):

    R1 = r'(?P<R1>[aeiouáéíóú]([bcdfgjklmnñpqrstvwxyz]|ll|rr|ch)[aeiouüáéíóúy])'
    R2a = r'(?P<R2a>[aeiouáéíóú][pcbgf][rl][aeiouáéíóúy])'
    R2b = r'(?P<R2b>[aeiouáéíóú][dt][r][aeiouáéíóúy])'
    R2c = r'(?P<R2c>[aeiouáéíóú][bcdefghjklmnñpqrstvwxyz][bcdefghjklmnpqrstvwxyz][aeiouáéíóúy])'
    R3a = r'(?P<R3a>[aeiouáéíóú][bcdefghjklmnñpqrstvwxyz](([pcbgf][rtl])|([dt][r]))[aeiouáéíóúy])'
    R3b = r'(?P<R3b>[aeiouáéíóú][bdnmlr][s][bcdefghjklmnñpqrstvwxyz][aeiouáéíóúy])'
    R3c = r'(?P<R3c>[aeiouáéíóú][s][t][bcdefghjklmnñpqrstvwxyz][aeiouáéíóúy])'
    R4a = r'(?P<R4a>[aeiouáéíóú](([bdnmlr][s]|[s][t]))[pcbgf][rl][aeiouáéíóúy])'
    '''
    R5a1 = r'(?P<R5a1>[aeoáéó]h?[iu])')
    R5a2 = r'(?P<R5a2>[iu]h?[aeoáéó])'
    R5a3 = r'(?P<R5a3>(([ií]h?[uúü])|([úuü]h?[ií])))'
    '''
    R5b1 = r'(?P<R5b1>(([aeo]h?[úí])|([úí]h?[aeo])))'
    R5b2 = r'(?P<R5b2>[aá][aá]|[eé][ée]|[ií][íi]|[oó][oó]|[uú][úu])'
    R5b3 = r'(?P<R5b3>(([aá]|[eé]|[oó])([oó]|[aá]|[eé])))'
    R5c = r'(?P<R5c>([aeiouáéíóú]h[aeiouáéíóúy]))'
    R6a = r'(?P<R6a>[iu][aeoáéó][iuy])'

    R = "(?i)" + R1 + "|" + R2a + "|" + R2b + "|" + R2c + "|" + R3a + "|" + R3b + "|" + R3c + "|" + R4a + "|" + R5c + "|" + R6a  + "|" + R5b1 + "|" + R5b2 + "|" + R5b3
    er = re.compile(R)
    corteAnterior = 0
    silabas = []

    while corteAnterior < len(cadena):
        m = er.search(cadena, corteAnterior)
        if not m:
            break

        if m.group("R1"):
            corteActual = m.start() + 1
            if corteActual > corteAnterior:
                silabas.append(cadena[corteAnterior:corteActual])
                corteAnterior = corteActual

        elif m.group("R2a"):
            corteActual = m.start() + 1
            if corteActual > corteAnterior:
                silabas.append(cadena[corteAnterior:corteActual])
                corteAnterior = corteActual

        elif m.group("R2b"):
            corteActual = m.start() + 1
            if corteActual > corteAnterior:
                silabas.append(cadena[corteAnterior:corteActual])
                corteAnterior = corteActual

        elif m.group("R2c"):
            corteActual = m.start() + 2
            if corteActual > corteAnterior:
                silabas.append(cadena[corteAnterior:corteActual])
                corteAnterior = corteActual

        elif m.group("R3a"):
            corteActual = m.start() + 2
            if corteActual > corteAnterior:
                silabas.append(cadena[corteAnterior:corteActual])
                corteAnterior = corteActual

        elif m.group("R3b"):
            corteActual = m.start() + 3
            if corteActual > corteAnterior:
                silabas.append(cadena[corteAnterior:corteActual])
                corteAnterior = corteActual

        elif m.group("R3c"):
            corteActual = m.start() + 3
            if corteActual > corteAnterior:
                silabas.append(cadena[corteAnterior:corteActual])
                corteAnterior = corteActual

        elif m.group("R4a"):
            corteActual = m.start() + 3
            if corteActual > corteAnterior:
                silabas.append(cadena[corteAnterior:corteActual])
                corteAnterior = corteActual

        # sin ataque R5a1 R5a2 R5a3

        elif m.group("R5b1"):
            corteActual = m.start() + 1
            if corteActual > corteAnterior:
                silabas.append(cadena[corteAnterior:corteActual])
                corteAnterior = corteActual

        elif m.group("R5b2"):
            corteActual = m.start() + 1
            if corteActual > corteAnterior:
                silabas.append(cadena[corteAnterior:corteActual])
                corteAnterior = corteActual

        elif m.group("R5b3"):
            corteActual = m.start() + 1
            if corteActual > corteAnterior:
                silabas.append(cadena[corteAnterior:corteActual])
                corteAnterior = corteActual

        elif m.group("R5c"):
            corteActual = m.start() + 1
            if corteActual > corteAnterior:
                silabas.append(cadena[corteAnterior:corteActual])
                corteAnterior = corteActual

        elif m.group("R6a"):
            corteActual = m.start() + 4
            if corteActual > corteAnterior:
                silabas.append(cadena[corteAnterior:corteActual])
                corteAnterior = corteActual

    silabas.append(cadena[corteAnterior:])

    if silabas[-1] == "":
        silabas.pop()

    return silabas

def entonar(palabra):
    Rtildes = r'(?P<Rtildes>[áéíóú])'
    Raguda = r'(?P<aguda>[^nsaeiou]$)'
    Rllana = r'(?P<llana>[nsaeiou]$)'

    det = "(?i)" + Rtildes + "|" + Raguda + "|" + Rllana
    er = re.compile(det)

    m = er.search(palabra)

    def tilde(palabra):
        Ra = r'(?P<Ra>á)'
        Re = r'(?P<Re>é)'
        Ri = r'(?P<Ri>í)'
        Ro = r'(?P<Ro>ó)'
        Ru = r'(?P<Ru>ú)'
        Rtildes = "(?i)" + Ra + "|" + Re + "|" + Ri + "|" + Ro + "|" + Ru
        re_tildes = re.compile(Rtildes)
        m = re_tildes.search(palabra)
        if m.group("Ra"):
            sust = re_tildes.sub('A', palabra)
            return sust
        elif m.group("Re"):
            sust = re_tildes.sub('E', palabra)
            return sust
        elif m.group("Ri"):
            sust = re_tildes.sub('I', palabra)
            return sust
        elif m.group("Ro"):
            sust = re_tildes.sub('O', palabra)
            return sust
        elif m.group("Ru"):
            sust = re_tildes.sub('U', palabra)
            return sust

    def aguda(lista_de_silabas):
        Ra = r'(?P<Ra>a)'
        Re = r'(?P<Re>e)'
        Ri = r'(?P<Ri>i)'
        Ro = r'(?P<Ro>o)'
        Ru = r'(?P<Ru>u)'
        Rvocal = "(?i)" + Ra + "|" + Re + "|" + Ri + "|" + Ro + "|" + Ru
        Rvocales = re.compile(Rvocal)

        ultima_silaba = lista_de_silabas[-1]
        m = Rvocales.search(ultima_silaba)

        if m:
            vocal_con_tilde = m.group()
            vocal_mayuscula = vocal_con_tilde.upper()
            sust = Rvocales.sub(vocal_mayuscula, ultima_silaba, count=1)
            return lista_de_silabas[:-1] + [sust]

        return lista_de_silabas

    def llana(lista_de_silabas):
        Ra = r'(?P<Ra>a)'
        Re = r'(?P<Re>e)'
        Ri = r'(?P<Ri>i)'
        Ro = r'(?P<Ro>o)'
        Ru = r'(?P<Ru>u)'
        Rvocal = "(?i)" + Ra + "|" + Re + "|" + Ri + "|" + Ro + "|" + Ru
        Rvocales = re.compile(Rvocal)

        penultima_silaba = lista_de_silabas[-2]
        m = Rvocales.search(penultima_silaba)

        if m:
            vocal_con_tilde = m.group()
            vocal_mayuscula = vocal_con_tilde.upper()

            sust = Rvocales.sub(vocal_mayuscula, penultima_silaba, count=1) # count por que sino sustituye todo
            return lista_de_silabas[:-2] + [sust] + [lista_de_silabas[-1]]

        return lista_de_silabas

    if m.group("Rtildes"):
        return silabear(tilde(palabra))
    elif m.group("aguda"):
        return aguda(silabear(palabra))
    else:
        return llana(silabear(palabra))

def clasifica(palabra):
    Rmay = r'(?P<Rmay>[AEIOU])'
    may = re.compile(Rmay)
    en = entonar(palabra)
    if en:
        ultima = en[-1]
        m = may.search(ultima)
        if m:
            return " y es aguda"
        if len(en) > 1:
            penultima = en[-2]
            m1 = may.search(penultima)
            if m1:
                return " y es llana"
        if len(en) > 2:
            antepenultima = en[-3]
            m2 = may.search(antepenultima)
            if m2:
                return " y es esdrújula"
        if len(en) > 3:
                return " y es sobreesdrújula"

dicTod = dict()

def menu():
    try:
        f = open("dic.csv", "r", encoding="utf8")
        linea = f.readline()
        while linea:
            clave, valor1, valor2 = linea.strip().split(';')
            dicTod[clave] = [valor1, valor2]
            linea = f.readline()
        f.close()
    except FileNotFoundError:
        pass
    opcion = input("introduce opcion:\n 1 (silabear)\n 2 (entonar)\n 3 (exit)\n")
    try:
        opcion = int(opcion)
    except:
        print(f"{opcion} no es una opcion")
    if opcion == 1:
        palabra = input("Introduce una palabra para silabear:\n")
        palabra = palabra.lower()
        if palabra in dicTod:
            print("El resultado ya se encuentra en el diccionario y es: ", dicTod[palabra][0])
        else:
            print("Su silabeo es: ", silabear(palabra))
            dicTod[palabra] = [silabear(palabra), entonar(palabra)]
    elif opcion == 2:
        palabra = input("Introduce una palabra para clasificar según su entonación:\n")
        palabra = palabra.lower()
        if palabra in dicTod:
            print("El resultado ya se encuentra en el diccionario es : ", dicTod[palabra][1]) # eso
        else:
            print("El resultado es: ", entonar(palabra), clasifica(palabra))
            dicTod[palabra] = [silabear(palabra), entonar(palabra)]
    elif opcion == 3:
        fsal = open("dic.csv", 'w', encoding="utf8")
        for clave in dicTod.keys():
            valores = dicTod.get(clave)
            valores_cadena = [str(valor) for valor in valores]
            print(clave, ";".join(valores_cadena), file=fsal, sep=";")
        fsal.close()
        print("Adios!")
        exit(0)

if __name__ == "__main__":
    while True:
        menu()