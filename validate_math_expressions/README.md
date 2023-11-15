Dada uma String "Expression" que representa uma expressão aritmética, composta por variáveis (x, y, z), operadores binários (+, -, *, /) e parênteses; escreva uma função/método que receba como entrada a String "Expression" e verifique se esta representa uma expressão bem formada.
Uma expressão bem formada precisa atender aos seguintes requisitos:
-> Número de parênteses abrindo e fechando devem ser iguais
-> Varíaveis/expressões devem ser separadas por operadores binários (não podem existir duas variáveis separadas por parênteses)
Ex:
(x + y)             => expressão bem formadaø
(x + y) * z         => expressão bem formada
x - z + (y)         => expressão bem formada
(x * y) + (x * z)   => expressão bem formada
x ) y               => expressão inválida
(x)(y)              => expressão inválida
-> operadores binários devem separar variáveis/expressões. Não podem existir dois operadores binários seguidos, ou separados por parênteses
Ex:
x + y + z           => Expressão bem formada
(x) + (y) + (z * x) => Expressão bem formada
x + )               => Expressão inválida
(x) + (             => Expressão inválida
x + (* y)           => Expressão inválida
