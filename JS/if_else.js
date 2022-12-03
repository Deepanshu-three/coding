let custumerIsBanned = false;
let soup = "corn soup"
let reply;
let crackers = true;
if (custumerIsBanned){
    reply = "no soup for you"
}
else if (soup && crackers) {
    reply = "here is your order for soup and crackers"
}
else if (soup) {
    reply = `Here is your order of ${soup}`
}
else{
    reply = `sorry we dont have that cupprently ${soup}`
}
console.log(reply);