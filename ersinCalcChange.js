// def calc_change(n):
    
//     penny = 1
//     nickle = 5
//     dime = 10
//     quarter = 25
    
//     coins = {
//         quarter: 0,
//         dime: 0,
//         nickle: 0,
//         penny: 0
//     }
    
//     while n > 0:
//         if n >= quarter:
//             n -= 25
//             coins[quarter] += 1
//         elif n >= dime:
//             n -= 10
//             coins[dime] += 1
//         elif n >= nickle:
//             n -= 5
//             coins[nickle] += 1
//         else:
//             n -= penny
//             coins[penny] += 1
    
//     print coins
    
// calc_change(55)

function calcChange(n) {
  const penny = 1
  const nickle = 5
  const dime = 10
  const quarter = 25

  const coins = {
    quarter: 0,
    dime: 0,
    nickle: 0,
    penny: 0
  }

  while ( n > 0) {
    if (n >= quarter) {
      n -= quarter;
      coins.quarter += 1;

    } else if (n >= dime) {
      n -= dime;
      coins.dime += 1;

    } else if (n >= nickle) {
      n -= nickle;
      coins.nickle += 1;

    } else {
      n -= penny;
      coins.penny += 1;
    }
  }

return coins
}

console.log(calcChange(55))