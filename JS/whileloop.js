// let num = 0;
// while(num<=50){
//     console.log(num);
//     num++;
// }

// let num = 51;
// do {
//     console.log(num)
//     num++
// }while (num<=50);
name1 = "Deepanshu"
counter = 0;
while (counter<=5){
    if (counter === 1){
        counter+=2;
        continue;
    } 

    myletter = name1[counter];
    console.log(myletter);
    if (myletter === "s") break;
    counter++;
}