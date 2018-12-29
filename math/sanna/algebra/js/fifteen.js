function func1(x) {
  theFunc = 1 - Math.pow(x,2)
  console.log(theFunc);
}


function func2(x) {
  theFunc = Math.pow(Math.E, -x)
  console.log(theFunc);
}

answerArray1 = [func1(0.2), func1(0.4), func1(0.5), func1(0.8), func1(1), func1(1.2), func1(1.4), func1(1.5), func1(1.8), func1(2), func1(2.2), func1(2.4), func1(2.5)]
answerArray2 = [func2(0.2), func2(0.4), func2(0.5), func2(0.8), func2(1), func2(1.2), func2(1.4), func2(1.5), func2(1.8), func2(2), func2(2.2), func2(2.4), func2(2.5)]
