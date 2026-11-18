# 📘 Assignment: Searching and Sorting in Python

## 🎯 Objective

Implemente algoritmos de busca e ordenação em Python e compare a eficiência de diferentes estratégias. Ao final, você saberá quando usar busca binária e por que ela depende de uma lista ordenada.

## 📝 Tasks

### 🛠️ Implemente a busca linear

#### Descrição
Complete `linear_search()` para percorrer uma lista de números e localizar um valor-alvo.

#### Requisitos
O programa concluído deve:

- Retornar o índice da primeira ocorrência do valor-alvo.
- Retornar `-1` quando o valor não estiver na lista, inclusive quando a lista estiver vazia.
- Manter a lista original sem alterações.

### 🛠️ Ordene os valores com insertion sort

#### Descrição
Complete `insertion_sort()` para ordenar os números em ordem crescente usando o algoritmo insertion sort.

#### Requisitos
O programa concluído deve:

- Retornar uma nova lista em ordem crescente, sem alterar a lista original.
- Lidar corretamente com listas vazias, listas com um elemento e valores repetidos.
- Organizar os elementos por inserções, sem chamar `sort()` ou `sorted()`.

### 🛠️ Implemente a busca binária e compare

#### Descrição
Complete `binary_search()` para localizar um valor em uma lista já ordenada. Depois, compare quantas etapas os dois algoritmos de busca precisam em listas maiores.

#### Requisitos
O programa concluído deve:

- Retornar o índice de uma ocorrência do valor-alvo ou `-1` quando ele não estiver presente.
- Reduzir o intervalo de busca pela metade a cada etapa, sem percorrer a lista inteira.
- Usar busca binária somente com uma lista ordenada e explicar por que essa condição é necessária.
- Explicar que a busca linear pode verificar até `n` elementos e a busca binária até aproximadamente `log₂(n)` etapas.

Exemplo de uso:

```python
numbers = [2, 4, 6, 8, 10]
print(linear_search(numbers, 8))  # 3
print(binary_search(numbers, 8))  # 3
print(insertion_sort([5, 2, 4]))  # [2, 4, 5]
```