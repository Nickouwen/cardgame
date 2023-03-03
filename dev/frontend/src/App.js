import { useState } from "react";

function Instructions() {
  return (
    <div className="instructions">
      <span>Instructions:</span>
      <div className="instructions-text">
        This is the instructions text.
      </div>
    </div>
  )
}

function Score() {
  return (
    <div className="score">
      <span>Score:</span>
      <div className="score-text">
        This is the score text.
      </div>
    </div>
  )
}

function Card({ number, value, selected, onCardClick }) {
  return (
    <button className="card" onClick={onCardClick}>
      <div>{number}</div>
      <div>{value}</div>
      <div>{selected.toString()}</div>
    </button>
  );
}

function BullheadStack() {
  function handleClick() {
    console.log('bullhead clicked');
  }
  return <Card number="Bull" value="Head" selected={false} onCardClick={handleClick} />;
}

function Hand({ cards, selectedCard, onCardClick }) {
  const handItems = cards.map(card =>
    <Card key={card.number}
      number={card.number}
      value={card.pointValue}
      selected={card.number === selectedCard}
      onCardClick={() => onCardClick(card.number)} />
  );
  return (
    <div className="player-hand">{handItems}</div>
  );
}

function Pile({ number, cards, onCardClick }) {
  const pileCards = cards.map(card =>
    <Card key={card.number} number={card.number} value={card.pointValue} selected={false} onCardClick={() => onCardClick(card.number)} />
  );

  return (
    <div className="table-pile">
      <div className="pile-label">Pile {number}:</div>
      <div className="pile-items">{pileCards}</div>
    </div>
  );
}

function Player({ playerNumber, handCards }) {
  const [cardSelected, setCardSelected] = useState(-1);

  function handleClick(number) {
    if (cardSelected === number) {
      setCardSelected(-1);
      console.log('clicked ' + number.toString());
    }
    else {
      setCardSelected(number);
      console.log('clicked ' + number.toString());
    }
  }

  return (
    <div className="player">
      <div>
        <BullheadStack />
      </div>
      <div>
        <Hand cards={handCards} selectedCard={cardSelected} onCardClick={handleClick} />
        Player {playerNumber} Name
      </div>
    </div>
  );
}

function Table({ pileCards, onPileClicked }) {
  let table = [];
  for (let i = 0; i < 4; i++) {
    table.push(<Pile key={i + 1} number={i + 1} cards={pileCards[i]} onCardClick={() => onPileClicked(i + 1)} />)
  }
  return (
    <div className="table">
      {table}
    </div>
  );
}

function Cardgame() {
  const handCards1 = [
    { number: 3, pointValue: 1 },
    { number: 11, pointValue: 5 },
    { number: 55, pointValue: 7 }
  ];

  const handCards2 = [
    { number: 1, pointValue: 1 },
    { number: 22, pointValue: 5 },
    { number: 100, pointValue: 3 }
  ];

  const pileCards = [[
    { number: 8, pointValue: 1 },
    { number: 35, pointValue: 2 },
    { number: 40, pointValue: 3 },
    { number: 77, pointValue: 5 },
    { number: 89, pointValue: 1 },
  ],
  [
    { number: 9, pointValue: 1 },
    { number: 25, pointValue: 2 },
    { number: 50, pointValue: 3 },
    { number: 66, pointValue: 5 },
    { number: 98, pointValue: 1 },
  ],
  [
    { number: 2, pointValue: 1 },
    { number: 15, pointValue: 2 },
    { number: 20, pointValue: 3 },
    { number: 33, pointValue: 5 },
    { number: 46, pointValue: 1 },
  ],
  [
    { number: 4, pointValue: 1 },
    { number: 5, pointValue: 2 },
    { number: 60, pointValue: 3 },
    { number: 88, pointValue: 5 },
    { number: 93, pointValue: 1 },
  ]];

  function handlePileClicked(pileNumber) {
    console.log('Pile clicked ' + pileNumber);
  }

  return (
    <>
      <Player key={1} playerNumber={1} handCards={handCards1} />
      <Table pileCards={pileCards} onPileClicked={handlePileClicked} />
      <Player key={2} playerNumber={2} handCards={handCards2} />
    </>
  );
}

// function Square({ value, onSquareClick }) {
//   return (
//     <button className="square" onClick={onSquareClick}>
//       {value}
//     </button>
//   );
// }

// function Board({ xIsNext, squares, onPlay }) {
//   function handleClick(i) {
//     if (squares[i] || calculateWinner(squares)) {
//       return;
//     }
//     const nextSquares = squares.slice();
//     if (xIsNext) {
//       nextSquares[i] = "X";
//     }
//     else {
//       nextSquares[i] = "O";
//     }
//     onPlay(nextSquares);
//   }

//   const winner = calculateWinner(squares);
//   let status;
//   if (winner) {
//     status = "Winner: " + winner;
//   }
//   else {
//     status = "Next player: " + (xIsNext ? "X" : "O");
//   }

//   let board = []
//   for (let i = 0; i < 3; i++) {
//     let row = []
//     for (let j = 0; j < 3; j++) {
//       let k = i * 3 + j;
//       row.push(<Square key={k} value={squares[k]} onSquareClick={() => handleClick(k)} />);
//     }
//     board.push(<div key={i} className="board-row">{row}</div>);
//   }

//   return (
//     <>
//       <div className="status">{status}</div>
//       {board}
//     </>
//   );
// }

export default function Game() {
  // const [history, setHistory] = useState([Array(9).fill(null)]);
  // const [currentMove, setCurrentMove] = useState(0);
  // const xIsNext = currentMove % 2 === 0;
  // const currentSquares = history[currentMove];

  // function handlePlay(nextSquares) {
  //   const nextHistory = [...history.slice(0, currentMove + 1), nextSquares];
  //   setHistory(nextHistory);
  //   setCurrentMove(nextHistory.length - 1);
  // }

  // function jumpTo(nextMove) {
  //   setCurrentMove(nextMove);
  // }

  // const moves = history.map((squares, move) => {
  //   if (move === currentMove) {
  //     return (
  //       <li key={move}>
  //         You are at move #{move}
  //       </li>
  //     )
  //   }
  //   let description;
  //   if (move > 0) {
  //     description = 'Go to move #' + move;
  //   }
  //   else {
  //     description = 'Go to game start';
  //   }
  //   return (
  //     <li key={move}>
  //       <button onClick={() => jumpTo(move)}>{description}</button>
  //     </li>
  //   );
  // });

  return (
    <>
      <div className="cardgame">
        <div className="cardgame-left">
          <Instructions />
        </div>
        <div className="cardgame-centre">
          <Cardgame />
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

// function calculateWinner(squares) {
//   const lines = [
//     [0, 1, 2],
//     [3, 4, 5],
//     [6, 7, 8],
//     [0, 3, 6],
//     [1, 4, 7],
//     [2, 5, 8],
//     [0, 4, 8],
//     [2, 4, 6]
//   ];
//   for (let i = 0; i < lines.length; i++) {
//     const [a, b, c] = lines[i];
//     if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
//       return squares[a];
//     }
//   }
//   return null;
// }