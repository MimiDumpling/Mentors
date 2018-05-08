// """
// Translate a string into Leet Speak.

// leet = {
//     'a' : '@',
//     'e' : '3',
//     't' : '7',
//     'l' : '1',
//     'o' : '0'
// }

// """

// def leet_spk(string):
//     leet = {
//         'a' : '@',
//         'e' : '3',
//         't' : '7',
//         'l' : '1',
//         'o' : '0'
//         }

//     split_str = list(string)

//     for index, letter in enumerate(split_str):
//         if letter in leet:
//             split_str[index] = leet[letter]

//     return "".join(split_str)


// print "+++TESTS+++"
// print "Correct: '1337', Result: ", leet_spk("leet")
// print "Correct: 'W@zzup', Result: ", leet_spk("Wazzup")
// print "Correct: 'cup', Result: ", leet_spk("cup")
// print "Correct: ' ', Result: ", leet_spk(" ")

function leetSpeak(string) {
  leet = {
    'a' : '@',
    'e' : '3',
    't' : '7',
    'l' : '1',
    'o' : '0'
    }
  
  const splitString = string.split("")
  
  for(const index in splitString) {
    const item = splitString[index]
    if(leet.hasOwnProperty(item)) {
      splitString[index] = leet[item]
    }
  }
  return splitString.join("")
}

console.log(leetSpeak("leet"))
console.log(leetSpeak("Wazzup"))
console.log(leetSpeak("cup"))
console.log(leetSpeak(" "))