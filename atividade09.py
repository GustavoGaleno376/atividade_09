# Um motorista deseja calcular o consumo médio de combustível do seu carro. Crie um programa que receba a quantidade de quilômetros percorridos e a quantidade de litros de combustível consumidos, e calcule o consumo médio (km por litro).
distancia=float(input("quantos quilomentros você rodou?"))
combustivel=int(input("quantos litros você ultilizou"))
media= (distancia/100)*combustivel
print(f"sua media de litros por quilometro é {media} ")