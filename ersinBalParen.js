// """
// Write a function that takes in 
// a string. There are parentheses
// in the string. Return True if 
// the parentheses are balance.
// Return False if not.
// """

// def bal_par(string):
//     new_str = list(string)

//     opened = 0
//     closed = 0

//     for char in new_str:
//         if char == ")":
//             closed += 1
//             if closed > opened:
//                 return False
//         elif char == "(":
//             opened += 1

//     if opened == closed:
//         return True
//     else:
//         return False


function balanceParentheses(string){
    const array = string.split("")
    let opened = 0;
    let closed = 0;

    for (let character of array){
        if (character === ")"){
            closed += 1;
            if (closed > opened){
                return false;
            }
        } else if (character === "("){
            opened += 1;
        }
    }

    if (opened === closed){
        return true;
    } else {
        return false;
    }
}

console.log(balanceParentheses("((()))"))
console.log(balanceParentheses("(()))"))
console.log(balanceParentheses(")"))
console.log(balanceParentheses("((("))




