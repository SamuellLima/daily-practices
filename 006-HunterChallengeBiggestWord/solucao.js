function find_longest_word(phrase) {
  // main function; Finds and highlights the longest received word.
  if (!phrase) {
    return "enter a valid phrase";
  }
  return phrase.split(" ").reduce((a, b) => (a.length >= b.length ? a : b));
}

let phrase = "Just a common phrase for testing";
console.log(find_longest_word(phrase));
