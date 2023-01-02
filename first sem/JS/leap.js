function is_leap(year){
    if ((year%4==0) && (year%100!=0)||(year%400==0)){
        console.log(year+" is leap year")
    }
    else{
        console.log(year+"not a leap year")
    }
}

const year = prompt("Enter a year");

is_leap(year)