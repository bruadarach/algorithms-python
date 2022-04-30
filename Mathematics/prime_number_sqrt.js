/*

시간복잡도: O(sqrt(n))

알고리즘: 
- 1. 1은 소수가 아니므로 먼저 처리
- 2. 짝수는 소수가 아니므로 false 처리. (단, 2는 짝수이면서 유일한 소수이므로 예외처리 필요)
- 3. 2 ~ N제곱근까지 나눠본 후 하나라도 나눠떨어지는 것이 존재하면 false
- n제곱근까지 나눴음에도 나눠떨어지지 않는 경우는 소수임

제곱근을 사용하는 방법

- N의 약수는 무조건 sqrt(N)의 범위에 존재한다.

- 만약 N이 12라 할때, 12의 제곱근은 약 3.46이다.
  12의 약수는 1, 2, 3, 4, 6, 12 이다.
  여기서 1과 12를 제외했을 때 이는 2 * 6, 3 * 4, 4 * 3, 6 * 2의 결과이다.

- 이들의 관계는 몫이 커지면 나누는 값이 작아지거나 나누는 값이 커지만 몫이 작아지는 반비례 관계이다. 
  결국 N의 절반(제곱근)까지 향하게 되면 이후 몫과 나누는 값이 반대로 바뀌게만 되는 상황이다.

- 따라서 N의 제곱근까지 나누어 떨어지는지 여부(=약수가 있는지 여부)를 조사하면 더 빠르게 소수판별을 할 수 있다.
  (소수는 1과 자기자신 이외에는 약수를 갖지 않음!)

*/

function isPrime(n) {
    console.log(n);
    console.log(Math.sqrt(n));
      if(n <= 1){
          return false; // 1은 소수가 아님.
      }
      // 짝수는 소수에서 제외
      // 단, 2는 유일하게 짝수 중에서 소수
      if( n%2 === 0) {
          return n==2 ? true : false;
      }
      // n이 홀수인 경우, sqrt(n)까지 나눠서 나눠떨어지는지 여부 체크
      for(let i=3; i<=Math.sqrt(n); i += 2) { // 3,5,7,9,11 
        console.log(i)
          // 나눠 떨어진다면 약수에 해당하므로 소수가 아님.
          if( n % i == 0)
              return false;
      }
      // 위에서 걸러지지 않은 나머지 경우는 소수에 해당됨
      return true; 
  }
  
  console.log(isPrime(11)); // true
  console.log(isPrime(121)); // false
  
  