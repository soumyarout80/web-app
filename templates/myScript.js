

function trailing_zeros_factorial() {
    var n = document.getElementById('a').value;
    let result = 0;
    for (let i = 5; i <= n; i += 5) {
        let num = i;
        while (num % 5 === 0) {
            num /= 5;
            result++;
        }
    }
    alert(result);
  }