// Implement merge sort. 
// Merge sort takes two lists (sorted or unsorted), merges
// the lists and sorts them.

// Examples:
    
//     # odds and evens, length even
//     >>> merge_sort([1, 3, 5, 2, 4, 6])
//     [1, 2, 3, 4, 5, 6]

//     # already sorted, length odd
//     >>> merge_sort([2, 3, 4])
//     [2, 3, 4]

//     # one num off, length even
//     >>> merge_sort([3, 1, 2, 4, 5, 6])
//     [1, 2, 3, 4, 5, 6]

//     # one num, length odd
//     >>> merge_sort([1])
//     [1]

// def merge_sort(lst):
//     """Merge sort list --break into pieces-- and return result."""

//     # Base Case: Break everything down into a list of one
//     if len(lst) < 2:  # if length of lst is 1, return lst
//         return lst

//     mid = int(len(lst) / 2)  # index at half the list
//     lst1 = merge_sort(lst[:mid])  # divide list in half
//     lst2 = merge_sort(lst[mid:])  # assign other half

//     return make_merge(lst1, lst2)

// def make_merge(lst1, lst2):
//     """Merge two lists."""

//     result = []
//     index1 = 0
//     index2 = 0

//     while index1 < len(lst1) and index2 < len(lst2):
//         if lst1[index1] < lst2[index2]:
//             result.append(lst1[index1])
//             index1 += 1
//         else:
//             result.append(lst2[index2])
//             index2 += 1

//     if index1 < len(lst1):
//         result.extend(lst1[index1:])

//     if index2 < len(lst2):
//         result.extend(lst2[index2:])

//     return result

// if __name__ == '__main__':
//     print merge_sort([1, 3, 5, 2, 4, 6])

function mergeSort(array) {
    // Base Case
    if(array.length < 2) {
        return array
    }

    // why not Number(array.length / 2)???
    const mid = Math.floor(array.length / 2)
    const array1 = mergeSort(array.slice(0, mid))
    const array2 = mergeSort(array.slice(mid))

    console.log(`this is array1: `, array1)
    console.log(`this is array2: `, array2)
    return makeMerge(array1, array2)
}

function makeMerge(array1, array2) {
    let result = []
    let index1 = 0
    let index2 = 0

    while(index1 < array1.length && index2 < array2.length) {
        if(array1[index1] < array2[index2]) {
            result.push(array1[index1]);
            index1 ++;
        }else {
            result.push(array1[index2]);
            index2 ++;
        }
    }

    // if(index1 < array1.length) {
    //     result.push(array1.slice(index1))
    // }

    // if(index2 <array2.length) {
    //     result.push(array2.slice(index2))
    // }

    // return result

    return result.concat(array1.slice(index1)).concat(array2.slice(index2))
}

console.log(mergeSort([3, 1, 4, 2]))