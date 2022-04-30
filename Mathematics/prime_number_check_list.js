function listPrimes(num) {
  
    let result = "2"
    
    if (num > 2) {
      for (let n = 3; n <= num; n++) {//3 4 5
        if (n % 2 !==0 ) {
          for (let k=2; k < n; k++) {//2 23 234
            if (n%k === 0){
              break
            }
            else if (k+1 === n) {
              result = result + '-' + n
            }
          }
        } 
      } 
    }
    return result
  }

let output = listPrimes(2);
console.log(output); // --> '2'

output = listPrimes(6);
console.log(output); // --> '2-3-5'

output = listPrimes(18);
console.log(output); // --> '2-3-5-7-11-13-17'