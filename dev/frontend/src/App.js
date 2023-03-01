import { useState } from "react";

const handCards = [
  { number: 3, point_value: 1 },
  { number: 11, point_value: 5 },
  { number: 55, point_value: 7 }
];

const pileCards = [
  { number: 8, point_value: 1 },
  { number: 35, point_value: 2 },
  { number: 40, point_value: 3 },
  { number: 77, point_value: 5 },
  { number: 89, point_value: 1 },
];

function Instructions() {
  return (
    <div className="instructions">
      <span>Instructions:</span>
      <text className="instructions-text">
        This is the instructions text.
      </text>
    </div>
  )
}

function Score() {
  return (
    <div className="score">
      <span>Score:</span>
      <text className="score-text">
        This is the score text.
      </text>
    </div>
  )
}

function Card({ number, value }) {
  return <button className="card"><div>{number}</div><div>{value}</div></button>
}

function BullheadStack() {
  return <Card number="Bull" value="Head" />;
}

function Hand() {
  const handItems = handCards.map(card =>
    <Card key={card.number} number={card.number} value={card.point_value} />
  );
  return (
    <div className="player-hand">{handItems}</div>
  );
}

function Pile() {
  const pileItems = pileCards.map(card =>
    <Card key={card.number} number={card.number} value={card.point_value} />
  );
  return (
    <div className="table-pile">
      <div className="pile-label">Pile 1:</div>
      <div className="pile-items">{pileItems}</div>
    </div>
  );
}

function Player() {
  return (
    <div className="player">
      <div>
        <BullheadStack />
      </div>
      <div>
        <Hand />
        Player 1 Name
      </div>
    </div>
  );
}

function Table() {
  return (
    <div className="table">
      <Pile />
      <Pile />
      <Pile />
      <Pile />
    </div>
  );
}

function Square({ value, onSquareClick }) {
  return (
    <button className="square" onClick={onSquareClick}>
      {value}
    </button>
  );
}

function Board({ xIsNext, squares, onPlay }) {
  function handleClick(i) {
    if (squares[i] || calculateWinner(squares)) {
      return;
    }
    const nextSquares = squares.slice();
    if (xIsNext) {
      nextSquares[i] = "X";
    }
    else {
      nextSquares[i] = "O";
    }
    onPlay(nextSquares);
  }

  const winner = calculateWinner(squares);
  let status;
  if (winner) {
    status = "Winner: " + winner;
  }
  else {
    status = "Next player: " + (xIsNext ? "X" : "O");
  }

  let board = []
  for (let i = 0; i < 3; i++) {
    let row = []
    for (let j = 0; j < 3; j++) {
      let k = i * 3 + j;
      row.push(<Square key={k} value={squares[k]} onSquareClick={() => handleClick(k)} />);
    }
    board.push(<div key={i} className="board-row">{row}</div>);
  }

  return (
    <>
      <div className="status">{status}</div>
      {board}
    </>
  );
}

export default function Game() {
  const [history, setHistory] = useState([Array(9).fill(null)]);
  const [currentMove, setCurrentMove] = useState(0);
  const xIsNext = currentMove % 2 === 0;
  const currentSquares = history[currentMove];

  function handlePlay(nextSquares) {
    const nextHistory = [...history.slice(0, currentMove + 1), nextSquares];
    setHistory(nextHistory);
    setCurrentMove(nextHistory.length - 1);
  }

  function jumpTo(nextMove) {
    setCurrentMove(nextMove);
  }

  const moves = history.map((squares, move) => {
    if (move === currentMove) {
      return (
        <li key={move}>
          You are at move #{move}
        </li>
      )
    }
    let description;
    if (move > 0) {
      description = 'Go to move #' + move;
    }
    else {
      description = 'Go to game start';
    }
    return (
      <li key={move}>
        <button onClick={() => jumpTo(move)}>{description}</button>
      </li>
    );
  });

  return (
    <>
      <div className="cardgame">
        <div className="cardgame-left">
          <Instructions />
        </div>
        <div className="cardgame-centre">
          <Player />
          <Table />
          <Player />
        </div>
        <div className="cardgame-right">
          <Score />
        </div>
      </div>
      {/* <div className="game">
        <div className="game-board">
          <Board xIsNext={xIsNext} squares={currentSquares} onPlay={handlePlay} />
        </div>
        <div className="game-info">
          <ol>{moves}</ol>
        </div>
      </div> */}
    </>
  )
}

function calculateWinner(squares) {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
  ];
  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null;
}