const numbers = [2, 11, 159684, 4898, 84848486, 7, 48489]; // Trocado a ordem para um melhor teste
const target = 9;

function findTwoSum(nums, target) {
  // 1. Crie um objeto para armazenar os números que já vimos e seus índices.
  const seenNumbers = {}; // Ex: { 2: 0, 7: 1, ... }

  // 2. Percorra o array de números com um loop 'for' corrigido.
  for (let i = 0; i < nums.length; i++) {
    const currentNumber = nums[i];
    
    // 3. Calcule o complemento (o número que falta para atingir o alvo).
    const complement = target - currentNumber;

    // 4. Verifique se o complemento JÁ EXISTE no nosso objeto de anotações.
    if (seenNumbers[complement] !== undefined) {
      // 5. Se existir, encontramos o par! Retorne o índice do complemento e o índice atual.
      return [seenNumbers[complement], i];
    }

    // 6. Se não encontrou o par, adicione o número atual e seu índice ao objeto.
    seenNumbers[currentNumber] = i;
  }
}

const result = findTwoSum(numbers, target);
console.log(result); // Saída esperada: [0, 2]