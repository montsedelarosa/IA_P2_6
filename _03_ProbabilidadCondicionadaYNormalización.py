# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

# Definir las probabilidades a priori P(A) y P(B)
probabilidad_A = 0.4
probabilidad_B = 0.6

# Definir la probabilidad condicionada P(B|A), que es la probabilidad de B dado que A ha ocurrido
probabilidad_condicionada_B_dado_A = 0.7

# Calcular la probabilidad conjunta P(A y B) usando la probabilidad condicionada
probabilidad_conjunta_A_y_B = probabilidad_A * probabilidad_condicionada_B_dado_A

# Calcular la probabilidad condicionada P(A|B) usando la probabilidad conjunta y P(B)
probabilidad_condicionada_A_dado_B = probabilidad_conjunta_A_y_B / probabilidad_B

# Imprimir los resultados
print(f"P(A): {probabilidad_A:.2f}")
print(f"P(B): {probabilidad_B:.2f}")
print(f"P(B|A): {probabilidad_condicionada_B_dado_A:.2f}")
print(f"P(A y B): {probabilidad_conjunta_A_y_B:.2f}")
print(f"P(A|B): {probabilidad_condicionada_A_dado_B:.2f}")
