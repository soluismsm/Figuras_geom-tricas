"""
Desenvolver um programa que utilize a biblioteca math para calcular e exibir
informações sobre figuras geométricas
"""
from os import system
from time import sleep
import math

SHAPES = ["Q", "C", "R", "L", "T"]
SHAPES_NAMES = ["Quadrado", "Círculo", "Retângulo", "Losango", "Triângulo"]
PI = math.pi
ESCOLHAS = [1, 2, 3, 4, 5]


def get_geometric_shape():
    """Pega o formato geométrico que o usuário vai usar.

    Returns:
        string: Nome da forma escolhida pelo usuário.
    """
    while True:
        print(
            "Qual é a figura geométrica?\n"
            "[Q]Quadrado\n"
            "[C]Círculo\n"
            "[R]Retângulo\n"
            "[L]Losango\n"
            "[T]Triângulo\n"
        )
        figura = input("Escolha uma figura (Q/C/R/L/T): ")

        # Verifica se a forma é válida.
        if figura.upper() not in SHAPES:
            print("Escolha uma forma geométrica válida.")
            continue

        for i in range(len(SHAPES)):
            if figura.upper() == SHAPES_NAMES[i][0]:
                figura_nome = SHAPES_NAMES[i]

        return figura_nome


def choose_options(forma):
    while True:
        print("Escolha uma opção:")
        print(f"[{ESCOLHAS[0]}]Ver área do {forma}.")
        print(f"[{ESCOLHAS[1]}]Ver perímetro do {forma}.")
        if forma == "Triângulo":
            print(f"[{ESCOLHAS[2]}]Mostrar tipo de triângulo.")
            print(f"[{ESCOLHAS[3]}]Escolher outra forma geométrica.")
            print(f"[{ESCOLHAS[4]}]Sair")
        else:
            print(f"[{ESCOLHAS[2]}]Escolher outra forma geométrica.")
            print(f"[{ESCOLHAS[3]}]Sair")
        escolha = input("O que quer fazer? ")
        # Verifica se a escolha está dentro das opções e se é um número
        try:
            escolha = int(escolha)
            if escolha not in ESCOLHAS:
                print("Digite uma opção válida.")
                continue
        except ValueError:
            print(f"Digite apenas um número de [{ESCOLHAS[0]}-{ESCOLHAS[-1]}]")

        return escolha


def formatter(txt):
    while True:
        user_input = input(txt)
        if user_input.strip() != "":
            try:
                user_input = float(user_input)
                if user_input > 0:
                    return user_input
            except ValueError:
                print("Digite um número válido (ou Enter)")
        return 0


def calculate_area(forma):
    while True:
        system("cls")
        if forma == "Quadrado":
            lados = valores["lados"]
            if lados != 0:
                area = math.pow(lados, 2)
                return area
        elif forma == "Círculo":
            raio = valores["raio"]
            if raio != 0:
                area = PI * math.pow(raio, 2)
                return area
        elif forma == "Retângulo" or forma == "Triângulo":
            base = valores["base"]
            altura = valores["altura"]
            if base != 0 and altura != 0:
                if forma == "Retângulo":
                    area = base * altura
                    return area
                area = (base * altura) / 2
                return area
        elif forma == "Losango":
            d1 = valores["d1"]
            d2 = valores["d2"]
            if d1 != 0 and d2 != 0:
                area = (d1 * d2) / 2
                return area

        print("Valores não preenchidos!")
        obter_valores(forma)
        continue


def calculate_perimeter(forma):
    while True:
        if forma == "Quadrado" or forma == "Losango":
            lados = valores["lados"]
            if lados != 0:
                perímetro = lados * 4
                return perímetro
        elif forma == "Círculo":
            raio = valores["raio"]
            if raio != 0:
                perímetro = 2 * PI * raio
                return perímetro
        elif forma == "Retângulo":
            base = valores["base"]
            altura = valores["altura"]
            if base != 0 and altura != 0:
                perímetro = 2 * (base + altura)
                return perímetro
        elif forma == "Triângulo":
            l1 = valores["l1"]
            l2 = valores["l2"]
            l3 = valores["l3"]
            if l1 != 0 and l2 != 0 and l3 != 0:
                perímetro = l1 + l2 + l3
                return perímetro

        print("Valores não preenchidos!")
        obter_valores(forma)


def verifica_triangulo(forma):
    while True:
        l1 = valores["l1"]
        l2 = valores["l2"]
        l3 = valores["l3"]
        if l1 != 0 and l2 != 0 and l3 != 0:
            print(f"Lados = Primeiro Lado: {l1}")
            print(f"\tSegundo Lado:  {l2}")
            print(f"\tTerceiro Lado: {l3}")
            # Triângulo Equilátero
            if l1 == l2 == l3:
                print("O valor de todos os lados são congruentes.")
                print("Logo é um Triângulo Equilátero\n")
                return
            # Triângulo Isósceles
            if l1 == l2 or l1 == l3 or l2 == l3:
                print("O valor de dois dos lados são congruentes.")
                print("Logo é um Triângulo Isósceles\n")
                return
            # Triângulo Escaleno
            if l1 != l2 and l1 != l3 and l2 != l3:
                print("O valor de todos os lados tem medidas distintas.")
                print("Logo é um Triângulo Escaleno\n")
                return

        print("Valores não preenchidos!")
        obter_valores(forma)


def obter_valores(forma):
    # Lados do Quadrado e Losango
    if forma == "Quadrado" or forma == "Losango" and valores["lados"] == 0:
        lados = formatter(f"Qual o valor dos lados do {forma}? L=")
        valores["lados"] = lados
    # Base e Altura do Retângulo e Triângulo
    if (
        forma == "Retângulo"
        or forma == "Triângulo"
        and (valores["base"] == 0 or valores["altura"] == 0)
    ):
        base = formatter("Qual a base do retângulo? b=")
        altura = formatter("Qual a altura do retângulo? h=")
        valores["base"] = base
        valores["altura"] = altura
    # Raio do Círculo
    if forma == "Círculo" and valores["raio"] == 0:
        raio = formatter("Qual o raio do círculo? r=")
        valores["raio"] = raio
    # Diagonal maior e menor do Losango
    if forma == "Losango" and (valores["d1"] == 0 or valores["d2"] == 0):
        d1 = formatter("Qual é a diagonal maior do losango? D=")
        d2 = formatter("Qual é a diagonal menor do losango? d=")
        valores["d1"] = d1
        valores["d2"] = d2
    # 3 Lados do Triângulo
    if forma == "Triângulo" and (
        valores["d1"] == 0 or valores["d2"] == 0 or valores["d3"] == 0
    ):
        l1 = formatter("Qual valor do primeiro lado do triângulo? l1=")
        l2 = formatter("Qual valor do segundo lado do triângulo? l2=")
        l3 = formatter("Qual valor do terceiro lado do triângulo? l3=")
        valores["l1"] = l1
        valores["l2"] = l2
        valores["l3"] = l3


def main():
    global valores
    exit = False
    while not exit:
        valores = {
            "lados": 0,
            "raio": 0,
            "base": 0,
            "altura": 0,
            "d1": 0,
            "d2": 0,
            "l1": 0,
            "l2": 0,
            "l3": 0,
        }
        forma = get_geometric_shape()
        obter_valores(forma)
        system("cls")

        while True:
            print(f"A sua forma é um {forma}")
            escolha = choose_options(forma)
            system("cls")

            if forma != "Triângulo":
                # Calcula area da forma geométrica
                if escolha == 1:
                    area = calculate_area(forma)
                    print(f"A área do {forma} é {area:.1f}\n")
                # Calcula perímetro da forma geométrica
                elif escolha == 2:
                    perímetro = calculate_perimeter(forma)
                    print(f"O perímetro do {forma} é {perímetro:.1f}\n")
                # Escolhe outra figura geométrica
                elif escolha == 3:
                    break
                # Fecha o Programa
                else:
                    exit = True
                    print("Saindo...")
                    sleep(1.5)
                    break
            else:
                # Calcula area da forma geométrica
                if escolha == 1:
                    area = calculate_area(forma)
                    print(f"A área do {forma} é {area:.1f}\n")
                # Calcula perímetro da forma geométrica
                elif escolha == 2:
                    perímetro = calculate_perimeter(forma)
                    print(f"O perímetro do {forma} é {perímetro:.1f}\n")
                # Verifica tipo de triângulo
                elif escolha == 3:
                    verifica_triangulo(forma)
                # Escolhe outra figura geométrica
                elif escolha == 4:
                    break
                # Fecha o Programa
                else:
                    exit = True
                    print("Saindo...")
                    sleep(1.5)
                    break


main()
