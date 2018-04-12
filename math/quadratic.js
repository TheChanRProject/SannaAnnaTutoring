// Function to build the quadratic formula from scratch

function quadraticFormula(a,b,c) {
  numerator1 = -b + Math.sqrt(b^2 - 4*a*c)
  numerator2 = -b - Math.sqrt(b^2 - 4*a*c)
  denominator = 2*a
  posQuad = (numerator1/denominator)
  negQuad = (numerator2/denominator)
  answers = [posQuad, negQuad]
  console.log(answers);
}
quadraticFormula(9, -13, 4)
