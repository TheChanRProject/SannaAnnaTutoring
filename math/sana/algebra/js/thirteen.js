function func1(x) {
  theFunc = Math.pow(x,2) - 9
  console.log(theFunc);
}

function func2(x) {
  theFunc = (6*Math.sqrt(3)) / x
  console.log(theFunc);
}

answerArrayF1 = [func1(-1.7), func1(1.7), func1(-3.5), func1(3.5)]
answerArrayF2 = [func2(-1.7), func2(1.7), func2(-3.5), func2(3.5)]

console.log(answerArrayF1);
console.log(answerArrayF2);
