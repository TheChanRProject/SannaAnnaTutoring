function interceptedArc(x) {
  console.log(2*x);
}
interceptedArc(36)


function triangleInequality(a,b,c) {
  pyArgs = a**2 + b**2
  if (pyArgs == c**2) {
    console.log("True");
  }
  else {
    console.log("False");
  }
}
triangleInequality(6,8,11)
triangleInequality(10,24,25)
triangleInequality(7,24,26)
triangleInequality(8,15,17)




function interiorSum(n) {
  formula = (n-2)*180
  console.log(formula);
}
interiorSum(6)

function interiorAngle(n) {
  formula = ((n-2)*180)/n
  console.log(formula);
}
interiorAngle(9)
interiorAngle(7)
interiorAngle(8)
interiorAngle(10)

const c = Math.sqrt(Math.pow(30,2) + Math.pow(20, 2))
console.log(c);

const x = 182 / 8
console.log(2*x + 7);
