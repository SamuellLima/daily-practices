function cpf_validator(cpf) {
  const clean_numbers = cpf.match(/\d+/g);
  const clean_cpf = clean_numbers.join("");

  if (clean_cpf.length == 11) {
    let sum_all1 = 0;
    let sum_all2 = 0;

    //Validando o primeiro dígito.
    for (let qtd = 0; qtd < 9; qtd++) {
      const multiplication = parseInt(clean_cpf[qtd]) * (10 - qtd);
      sum_all1 += multiplication;
    }

    let rest = sum_all1 % 11;
    let penultimate_digit = 11 - rest;

    for (let qtd = 0; qtd < 10; qtd++) {
      const multiplication = parseInt(parseInt(clean_cpf[qtd] * (11 - qtd)));
      sum_all2 += multiplication;
    }

    let rest2 = sum_all2 % 11;
    let last_digit = 11 - rest2;

    if (last_digit == 10 || last_digit == 11) {
      last_digit == 0;
    }

    if (penultimate_digit == 1 || penultimate_digit == 11) {
      penultimate_digit == 0;
    }

    console.log(penultimate_digit);
    console.log(last_digit);

    if (clean_cpf[9] == penultimate_digit && clean_cpf[10] == last_digit) {
      console.log("CPF Válido!");
    } else {
      console.error("CPF inválido!");
    }
  } else {
    console.error("CPF invalido!");
  }
}
cpf = "870.868.570-33"; // Digite um CPF aqui.
cpf_validator(cpf);
