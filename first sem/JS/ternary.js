let soup = "Chicken noodle soup"
let isCustomerBanned = false;
let soupAccess = isCustomerBanned ? "Sorry no soup for you"
    : soup ? "here is your order"
        : "soor no soup today";
console.log(soupAccess)