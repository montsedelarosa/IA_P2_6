# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

# Definir las probabilidades a priori para dos eventos A y B
probabilidad_a_priori_A = 0.3
probabilidad_a_priori_B = 0.7

# Imprimir las probabilidades a priori
print(f"Probabilidad a priori de A: {probabilidad_a_priori_A:.2f}")
print(f"Probabilidad a priori de B: {probabilidad_a_priori_B:.2f}")

# Calcular la probabilidad a priori complementaria (P(no A) o P(B complementaria))
probabilidad_complementaria_A = 1 - probabilidad_a_priori_A
probabilidad_complementaria_B = 1 - probabilidad_a_priori_B

# Imprimir las probabilidades a priori complementarias
print(f"Probabilidad a priori complementaria de A: {probabilidad_complementaria_A:.2f}")
print(f"Probabilidad a priori complementaria de B: {probabilidad_complementaria_B:.2f}")
