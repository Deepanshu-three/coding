let playgame = confirm("SHall we play rock paper scissors?");
if (playgame) {
    let playerchoice = prompt("Please enter rock paper scissors.");
    if (playerchoice) {
        let playerone = playerchoice.trim().toLowerCase();
        if (
            playerone === "rock" ||
            playerone === "paper" ||
            playerone === "scissors"
        ) {
            let computerchoice = Math.floor(Math.random() * 3 + 1);
            let computer =
                computerchoice === 1 ? "rock"
                    : computerchoice === 2 ? "paper"
                        : "scissors"

            let result =
                playerone === computer ? "Tie game" :
                    playerone === "rock" && computer === "paper" ?
                        `player one: ${playerone}\nComputer: ${computer}\n Computer` :
                        playerone === "paper" && computer === "scissors" ? `
            player one: ${playerone}\n computer: ${computer}\n
            computer wins`:
                            playerone === "scissors" && computer === "rock" ?
                                `player one: ${playerone}\ncomputer: ${computer}\n 
            computer wins`
                                : `player one: ${playerone}\ncomputer: ${computer}\n
            player one wins`;
            alert(result);
            let playagain = confirm("Play again?");
            playagain ? location.reload() : alert("ok, thanks for playing")

        }
        else {
            alert("you have enterd the wrong statement");

        }
    } else {
        alert("i guess you changed your mind")
    }
}