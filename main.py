import math
import os

const_plank_ev = 4.136E-15
const_plank_joule = 6.626E-34
velocidade_luz = 3E8

def imprime_tela_inicial():
    print("\n**********************************************************")
    print("*************** ATOMO DE BOHR E QUANTIZACAO **************")
    print("**********************************************************")
    
    print("\nAutoria: Mariane S. Carvalho\tTurma: 610")

    print("\n--------------------------------------------------------------------------------------------------------------")
    print("\nEste programa visa auxiliar no entendimento e calculo de varias propriedades e fenomenos relacionados ao atomo de hidrogenio," + 
          "\nusando os principios da mecanica quantica, especificamente o modelo de Bohr. " + 
          "\nEle aborda varias caracteristicas do átomo de hidrogenio, "+ 
          "como energia, comprimento de onda e frequencia associados \na diferentes transicoes de niveis quanticos.")
    print()

    print("\n--------------------------------------------------------------------------------------------------------------")

def menu_nav():
    print("\nSelecione a entrada:\n\n\t1 - Propriedades do atomo de H a partir do numero quantico\n\t2 - Calcular  energia, comprimento de onda e frequencia do foton emitido/absorvido a partir do salto quantico (ni e nf)\n\t3 - Calcular o nivel inicial (ni) ou final (nf) na EMISSAO de um foton pelo atomo de H\n\t4 - Calcular o nivel inicial (ni) ou final (nf) na ABSORCAO de um foton pelo atomo de H\n\t5 - Calcular a energia do foton a partir do comprimento de onda (λ) ou frequencia\n\t6 - Calcular o comprimento de onda (λ) e a frequencia do foton a partir da energia\n\t7 - Encerrar programa")

def calcula_raio(num_quantico):
    raio = math.pow(num_quantico, 2) * 5.29e-11

    print(f"raio da orbita (r) = {raio:.2E} m")

def calcula_velocidade(num_quantico):
    velocidade = 2.187e6 / num_quantico

    print(f"velocidade (v) = {velocidade:.2E} m/s")


def calcula_energia_cinetica(num_quantico):
    energia_cinetica = 13.6 / math.pow(num_quantico, 2)

    print(f"energia cinetica (K) = {energia_cinetica:.2f} eV")

def calcula_energia_potencial(num_quantico):
    energia_potencial = -27.2 / math.pow(num_quantico, 2)

    print(f"energia potencial (U) = {energia_potencial:.2f} eV")

def calcula_energia_total(num_quantico):
    energia_total = -13.6 / math.pow(num_quantico, 2)

    print(f"energia total (E) = {energia_total:.2f} eV")

def calcula_comprimento_onda(num_quantico):
    velocidade = 2.187e6 / num_quantico
    massa_eletron = 9.11e-31
    
    comprimento_onda = const_plank_joule / (massa_eletron * velocidade)
    
    print(f"comprimento de onda (λ) = {comprimento_onda:.2E} m")


def calcula_valores_salto_quantico(num_quantico_inicial, num_quantico_final):
    energia_inicial = -13.6 / math.pow(num_quantico_inicial, 2)
    energia_final = -13.6 / math.pow(num_quantico_final, 2)

    energia_foton = abs(energia_final - energia_inicial)
    
    comprimento_onda = (4.136e-15 * 3e8) / energia_foton

    frequencia = energia_foton /4.136e-15
    

    print(f"energia do foton (Ef) = {energia_foton:.2f} eV")
    print(f"comprimento de onda (λ) = {comprimento_onda:.2E} m")
    print(f"frequencia (f) = {frequencia:.2E} Hz")

def calcula_nivel_inicial(num_quantico_final, parametro_opcional, tipo):
    energia_final = -13.6 / math.pow(num_quantico_final, 2)
    energia_foton = 0

    if parametro_opcional == 1:
        # calcula pela frequencia
        freq = float(input("digite o valor da frequencia, em Hz: "))
        energia_foton = const_plank_ev * freq
    else:
        # calcula pelo comprimento
        comprimento = float(input("digite o comprimento de onda (λ), em metros: "))
        energia_foton = (const_plank_ev * velocidade_luz) / comprimento
    
    if tipo == 1:
        # absorcao
        energia_inicial = energia_final - energia_foton
    else:
        # emissao
        energia_inicial = energia_final + energia_foton
    
    num_quantico_inicial = math.sqrt(-13.6 / energia_inicial)
    
    print(f"\nnivel inicial (ni) = {round(num_quantico_inicial)}")

def calcula_nivel_final(num_quantico_inicial, parametro_opcional, tipo):
    energia_inicial = -13.6 / math.pow(num_quantico_inicial, 2)
    energia_foton = 0

    if parametro_opcional == 1:
        # calcula pela frequencia
        freq = float(input("digite o valor da frequencia, em Hz: "))
        energia_foton = const_plank_ev * freq
    else:
        # calcula pelo comprimento
        comprimento = float(input("digite o comprimento de onda (λ), em metros: "))
        energia_foton = (const_plank_ev * velocidade_luz) / comprimento
    
    if tipo == 1:
        # absorcao
        energia_final = energia_inicial + energia_foton
    else:
        # emissao
        energia_final = energia_inicial - energia_foton
    
    num_quantico_final = math.sqrt(-13.6 / energia_final)
    
    print(f"\nnivel final (nf) = {round(num_quantico_final)}")
    
def calcula_energia_foton(parametro, valor):
    energia_foton_ev = 0
    energia_foton_joule = 0

    if parametro == 1:
        # calcula pela frequencia
        energia_foton_joule = const_plank_joule * valor
        energia_foton_ev = energia_foton_joule / 1.602e-19
    else:
        # calcula pelo comprimento
        energia_foton_joule = (const_plank_joule * velocidade_luz) / valor
        energia_foton_ev = energia_foton_joule / 1.602e-19

    print(f"Energia do foton (Ef) = {energia_foton_joule:.2E} J.s \tou \t(Ef) = {energia_foton_ev:.2f} eV")

def calcula_parametros_foton(valor, unidade):
    comprimento_onda = 0
    frequencia = 0

    if unidade == 1:
        frequencia = valor / const_plank_joule
        comprimento_onda = (const_plank_joule * velocidade_luz) / valor
    else:
        frequencia = valor / const_plank_ev
        comprimento_onda = (const_plank_ev * velocidade_luz) / valor

    print(f"frequencia (f) = {frequencia:.2E} Hz")
    print(f"comprimento de onda (λ) = {comprimento_onda:.2E} m")

def main():
    imprime_tela_inicial()

    while(True):
        menu_nav()

        input_menu = int(input("\nDigite a opcao desejada: "))

        print()

        if input_menu == 1:
            valor = int(input("Digite o valor de n: "))
            
            print()

            calcula_raio(valor)
            calcula_velocidade(valor)
            calcula_comprimento_onda(valor)
            calcula_energia_cinetica(valor)
            calcula_energia_potencial(valor)
            calcula_energia_total(valor)

        elif input_menu == 2:
            valor_inicial = int(input("Digite o valor de ni: "))
            valor_final = int(input("Digite o valor de nf: "))
            
            print()

            calcula_valores_salto_quantico(valor_inicial, valor_final)            
        
        elif input_menu == 3:
            valor = int(input("Gostaria de calcular: \n\n\t1 - nivel inicial (ni)\n\t2 - nivel final (nf)\n\nopcao: "))
            parametro = int(input("\nA partir da(o):\n\n\t1 - frequencia\n\t2 - comprimento de onda (λ)\n\nopcao: "))

            print()  
            
            if valor == 1:
                valor = int(input("Digite o nivel final: "))
                calcula_nivel_inicial(valor, parametro, 2)
            else:
                valor = int(input("Digite o nivel inicial: "))
                calcula_nivel_final(valor, parametro, 2)          

        elif input_menu == 4:
            valor = int(input("Gostaria de calcular: \n\n\t1 - nivel inicial (ni)\n\t2 - nivel final (nf)\n\nopcao: "))
            parametro = int(input("\nA partir da(o):\n\n\t1 - frequencia\n\t2 - comprimento de onda (λ)\n\nopcao: "))

            print()  
            
            if valor == 1:
                valor = int(input("Digite o nivel final: "))
                calcula_nivel_inicial(valor, parametro, 1)
            else:
                valor = int(input("Digite o nivel inicial: "))
                calcula_nivel_final(valor, parametro, 1)

        elif input_menu == 5:
            valor = int(input("Gostaria de calcular a partir da(o):\n\n\t1 - frequencia\n\t2 - comprimento de onda (λ)\n\nopcao: "))

            print()

            if valor == 1:
                valor = float(input("Digite o valor da frequencia, em Hz: "))
                calcula_energia_foton(1, valor)
            else:
                valor = float(input("Digite o comprimento da onda, em metros: "))
                calcula_energia_foton(2, valor)

        elif input_menu == 6:
            valor = int(input("Gostaria de fornecer o valor da energia em: \n\n\t1 - J.s\n\t2 - eV\n\nopcao: "))
            energia = float(input("Digite o valor da energia: "))
            print()

            if valor == 1:
                calcula_parametros_foton(energia, 1)
            else:
                calcula_parametros_foton(energia, 2)

        elif input_menu == 7:
            break

        print()
        os.system("pause")
    
main()
