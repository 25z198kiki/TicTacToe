const boardElement = document.getElementById("board");
const messageElement = document.getElementById("message");
const resetButton = document.getElementById("reset");

const winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
];

let board = Array(9).fill("");
let currentPlayer = "X";
let gameOver = false;

function createBoard() {
    boardElement.innerHTML = "";

    board.forEach((value, index) => {
        const button = document.createElement("button");
        button.className = "cell";
        button.type = "button";
        button.dataset.index = index;
        button.textContent = value;
        button.disabled = Boolean(value) || gameOver;
        button.addEventListener("click", () => handleMove(index));
        boardElement.appendChild(button);
    });
}

function handleMove(index) {
    if (gameOver || board[index]) {
        return;
    }

    board[index] = currentPlayer;
    updateBoard();

    if (checkWinner()) {
        messageElement.textContent = `Player ${currentPlayer} wins!`;
        gameOver = true;
        updateBoard();
        return;
    }

    if (checkDraw()) {
        messageElement.textContent = "It's a draw!";
        gameOver = true;
        updateBoard();
        return;
    }

    currentPlayer = currentPlayer === "X" ? "O" : "X";
    updateMessage();
}

function checkWinner() {
    return winningConditions.some(condition => {
        const [a, b, c] = condition;
        return board[a] && board[a] === board[b] && board[a] === board[c];
    });
}

function checkDraw() {
    return board.every(cell => cell !== "") && !checkWinner();
}

function updateMessage() {
    if (gameOver) {
        return;
    }
    messageElement.textContent = `Current player: ${currentPlayer}`;
}

function updateBoard() {
    createBoard();
}

function resetGame() {
    board = Array(9).fill("");
    currentPlayer = "X";
    gameOver = false;
    updateMessage();
    updateBoard();
}

resetButton.addEventListener("click", resetGame);

updateMessage();
createBoard();
