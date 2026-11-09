<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tres en Raya (Tic Tac Toe)</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #1a1a1a;
            color: #ffffff;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }
        h1 {
            margin-bottom: 10px;
            color: #4CAF50;
        }
        #status {
            font-size: 1.2rem;
            margin-bottom: 20px;
            height: 30px;
        }
        .board {
            display: grid;
            grid-template-columns: repeat(3, 100px);
            grid-template-rows: repeat(3, 100px);
            gap: 8px;
            background-color: #333;
            padding: 8px;
            border-radius: 12px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.5);
        }
        .cell {
            background-color: #2a2a2a;
            border: none;
            font-size: 2.5rem;
            font-weight: bold;
            color: #fff;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            border-radius: 8px;
            transition: background-color 0.2s, transform 0.1s;
        }
        .cell:hover {
            background-color: #3a3a3a;
        }
        .cell:active {
            transform: scale(0.95);
        }
        .cell.x {
            color: #2196F3;
        }
        .cell.o {
            color: #FF5722;
        }
        #reset-btn {
            margin-top: 25px;
            padding: 10px 20px;
            font-size: 1rem;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            transition: background-color 0.2s;
        }
        #reset-btn:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>

    <h1>Tres en Raya</h1>
    <div id="status">Tu turno (X)</div>
    
    <div class="board" id="board">
        <button class="cell" data-index="0"></button>
        <button class="cell" data-index="1"></button>
        <button class="cell" data-index="2"></button>
        <button class="cell" data-index="3"></button>
        <button class="cell" data-index="4"></button>
        <button class="cell" data-index="5"></button>
        <button class="cell" data-index="6"></button>
        <button class="cell" data-index="7"></button>
        <button class="cell" data-index="8"></button>
    </div>

    <button id="reset-btn" onclick="reiniciarJuego()">Reiniciar partida</button>

    <script>
        const tablero = document.getElementById('board');
        const statusText = document.getElementById('status');
        const celdas = document.querySelectorAll('.cell');

        let estadoJuego = ["", "", "", "", "", "", "", "", ""];
        let juegoActivo = true;
        const jugadorHumano = "X";
        const jugadorIA = "O";

        const condicionesGanadoras = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], // Filas
            [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columnas
            [0, 4, 8], [2, 4, 6]              // Diagonales
        ];

        celdas.forEach(celda => {
            celda.addEventListener('click', manejarClickCelda);
        });

        function manejarClickCelda(e) {
            const index = e.target.getAttribute('data-index');

            if (estadoJuego[index] !== "" || !juegoActivo || statusText.textContent.includes("IA")) {
                return;
            }

            realizarMovimiento(index, jugadorHumano);
            
            if (verificarGanador(jugadorHumano)) {
                statusText.textContent = "¡Has ganado! 🎉";
                juegoActivo = false;
                return;
            }

            if (estadoJuego.every(celda => celda !== "")) {
                statusText.textContent = "¡Empate! 🤝";
                juegoActivo = false;
                return;
            }

            // Turno de la IA
            statusText.textContent = "Pensando la IA (O)...";
            setTimeout(turnoIA, 500);
        }

        function realizarMovimiento(index, jugador) {
            estadoJuego[index] = jugador;
            celdas[index].textContent = jugador;
            celdas[index].classList.add(jugador.toLowerCase());
        }

        function turnoIA() {
            if (!juegoActivo) return;

            // IA busca movimiento aleatorio disponible
            let disponibles = estadoJuego
                .map((val, idx) => val === "" ? idx : null)
                .filter(val => val !== null);

            if (disponibles.length > 0) {
                let movimientoAleatorio = disponibles[Math.floor(Math.random() * disponibles.length)];
                realizarMovimiento(movimientoAleatorio, jugadorIA);

                if (verificarGanador(jugadorIA)) {
                    statusText.textContent = "¡La IA ha ganado! 🤖";
                    juegoActivo = false;
                    return;
                }

                if (estadoJuego.every(celda => celda !== "")) {
                    statusText.textContent = "¡Empate! 🤝";
                    juegoActivo = false;
                    return;
                }

                statusText.textContent = "Tu turno (X)";
            }
        }

        function verificarGanador(jugador) {
            return condicionesGanadoras.some(condicion => {
                return condicion.every(index => estadoJuego[index] === jugador);
            });
        }

        function reiniciarJuego() {
            estadoJuego = ["", "", "", "", "", "", "", "", ""];
            juegoActivo = true;
            statusText.textContent = "Tu turno (X)";
            celdas.forEach(celda => {
                celda.textContent = "";
                celda.classList.remove('x', 'o');
            });
        }
    </script>
</body>
</html>
