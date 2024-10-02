#4.13 – Buffet: Um restaurante do tipo buffet oferece apenas cinco tipos básicos
#de comida. Pense em cinco pratos simples e armazene-os em uma tupla.
#• Use um laço for para exibir cada prato oferecido pelo restaurante.
#• Tente modificar um dos itens e cerifique-se de que Python rejeita a mudança.
#• O restaurante muda seu cardápio, substituindo dois dos itens com pratos
#diferentes. Acrescente um bloco de código que reescreva a tupla e, em
#seguida, use um laço for para exibir cada um dos itens do cardápio revisado
pratos = ('lasanha', 'bolo', 'aspargo ao molho madeira', 'hot-dog', 'hamburguer')
for a in pratos: print(a)
# pratos[2] = 'sushi'  # Essa linha vai gerar um TypeError
pratos = ('lasanha', 'bolo', 'aspargo ao molho madeira', 'frango frito', 'PF')
print("\n")
for a in pratos: print(a)

