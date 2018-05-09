// from collections import defaultdict

// """
// Ransom Note:

// - string1 is the ransom you want to write
// - string2 is the magazine you have to cut out the letters (or words -- this is harder)
// - return True if there's enough magazine letters/words
// - else: False

// THIS SOLUTION SOLVES FOR LETTERS
// """

// def ransom_note(ransom, magazine):

//     available = defaultdict(int)

//     if len(ransom) > len(magazine):
//         return False

//     for letter in ransom:
//         available[letter] += 1

//     for letter in magazine:
//         available[letter] -= 1

//     for letter in ransom:
//         if available[letter] > 0:
//             return False

//     return True

// print "+++TESTS+++"
// print "1. Correct: False, Result: ", ransom_note("cat", "car")
// print "2. Correct: False, Result: ", ransom_note("Oh", "car")
// print "3. Correct: False, Result: ", ransom_note("Hello", "yo")
// print "4. Correct: False, Result: ", ransom_note("Hi", "")
// print "5. Correct: False, Result: ", ransom_note("Hi", " ")
// print "6. Correct: True, Result: ", ransom_note(" ", " ")
// print "7. Correct: True, Result: ", ransom_note("Meow", "Meow")
// print "8. Correct: False, Result: ", ransom_note("Meoow", "Meowwwww")
// # why doesn't "w" register as a neg num when we print dict?

// this solves for letters, not words
function ransomNote(ransom, magazine) {
  available = {}

  if (ransom.length > magazine.length) {
    return false
  }

  for (const letter of ransom) {
    available[letter] = (available[letter] || 0) + 1
  }
  // available.letter === available['letter']
  // available.letter !== available[letter]
  // const arr = ['hi', 'ho']
  // arr === { 0: 'hi', 1: 'ho' }
  
  for (const letter of magazine) {
    available[letter] = (available[letter] || 0) - 1
  }
  
  for (letter of ransom) {
    if (available[letter] > 0) {
      return false
    }
  }

  return true
}

console.log("+++TESTS+++")
console.log("1. Correct: False, Result: ", ransomNote("cat", "car"))
console.log("2. Correct: False, Result: ", ransomNote("Oh", "car"))
console.log("3. Correct: False, Result: ", ransomNote("Hello", "yo"))
console.log("4. Correct: False, Result: ", ransomNote("Hi", ""))
console.log("5. Correct: False, Result: ", ransomNote("Hi", " "))
console.log("6. Correct: True, Result: ", ransomNote(" ", " "))
console.log("7. Correct: True, Result: ", ransomNote("Meow", "Meow"))
console.log("8. Correct: False, Result: ", ransomNote("Meoow", "Meowwwww"))