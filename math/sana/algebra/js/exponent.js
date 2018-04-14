const answer = 3 * Math.pow(6,0)
console.log(answer);

const answer2 = Math.pow(3, -1) + Math.pow(2, -1)
console.log(answer2);
console.log(5/6);

const answer3 = 1 / (Math.pow(3, -2))
console.log(answer3);

const answer4 = Math.pow(0.5, -2)
console.log(answer4);

const answer7 = Math.pow(16, 0.5)
console.log(answer7);

const answer8 = Math.pow(81, 0.75)
console.log(answer8);

const answer9 = Math.pow(-32, 0.6)
console.log(answer9);

const answer11 = Math.pow(27, -0.666)
console.log(answer11);
console.log(1/9);

const answer12 = Math.pow(3, -2)
console.log(answer12);

const answer22 = Math.pow(9, 0.5)
console.log(answer22);

const answer23 = Math.log2(64)
console.log(answer23);

const answer24 = Math.log2(-32)
console.log(answer24);

function getBaseLog(x, y) {
  console.log(Math.log(y) / Math.log(x));
  return Math.log(y) / Math.log(x);

}
getBaseLog(9, 27)
getBaseLog(3,27)

function inGraph(x,y) {
  if (y == Math.pow(3, 2*x)) {
    console.log("true");
  }
  else {
    console.log("false");
  }
}
inGraph(-1,-9)
inGraph(1,9)
inGraph(0.5, 3)

const exp31ArrayX = [0, 4, 8, 12, 16]
const exp31ArrayY = [3, 5, 7, 11, 19]

function exp34(x) {
  formula = Math.pow(1.069, x) * 2500
  console.log(formula);
}
exp34(10)

function newtonCooling(t) {
  t0 = 0
  t1 = 140
  k = -0.0815
  formula = t0 + (t1 - t0)*Math.exp(k*t)
  console.log(formula);
}
newtonCooling(15)

function func37p1(x) {
  console.log(Math.sqrt(4*x + 2));
}
func37p1(1.1)
func37p1(1.2)
func37p1(1.3)
func37p1(1.4)
func37p1(1.5)

function func37p2(x) {
  console.log(Math.pow(x,3));
}
func37p2(1.1)
func37p2(1.2)
func37p2(1.3)
func37p2(1.4)
func37p2(1.5)
