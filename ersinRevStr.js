// """
// Write a function that reverses a string.
// Use as much memory as you want.
// """

// def reverse_str(string):

//     lst = list(string)

//     current = len(lst) - 1

//     new_lst = []

//     while current > -1:
//         new_lst.append(lst[current])
//         current -= 1
//         #print new_lst

//     return "".join(new_lst)

// function reverseString(str){
// 	const lst = str.split("");
// 	let current = lst.length;
// 	const new_lst = []

// 	while (current > -1){
// 		new_lst.push(lst[current]);
// 		current -= 1;
// 	}

// 	return new_lst.join("")
// }

function reverseString(str){
	const lst = str.split("");
	const new_lst = []

	for (let current = lst.length; current > -1; current--){
		new_lst.push(lst[current])
	}

	return new_lst.join("")
}

console.log(reverseString("cat"));
console.log(reverseString("my cat"));
console.log(reverseString(" "));
console.log(reverseString(""));
console.log(reverseString("123"));
