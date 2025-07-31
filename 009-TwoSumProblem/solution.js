

const numbers = [2, 11, 7, 15];
const target = 9;


function find_position_numbers(numbers, target) { 

    const seen_numbers = {};

    for (let position = 0; position < numbers.length; position++){
        let number = numbers[position];

        let subtracted = target - number;

        if (seen_numbers[subtracted] !== undefined){
            return [seen_numbers[subtracted], position]
        }

        seen_numbers[number] = position;
}
 
}
result = find_position_numbers(numbers, target)
console.log(result)

    