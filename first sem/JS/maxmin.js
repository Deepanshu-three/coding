const num1 = parseInt(prompt("Enter first number: "));
const num2 = parseInt(prompt("Enter second number: "));
const num3 = parseInt(prompt("Enter third number: "));
let largest;
let smallest;

if(num1 >= num2 && num1 >= num3) {
    largest = num1;
}
else if (num2 >= num1 && num2 >= num3) {
    largest = num2;
}
else {
    largest = num3;
}
let str = largest+''
let result = str.bold()
document.write("MAXIMUM = "+result+'<br>')


if(num1 <= num2 && num1 <= num3) {
    smallest = num1;
}
else if (num2 <= num1 && num2 <= num3) {
    smallest = num2;
}
else {
    smallest = num3;
}

let str1 = smallest+''
let result1 = str1.bold();
document.write("MINIMUM = ",result1)