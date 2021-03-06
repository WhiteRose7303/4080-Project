var BUTTON_BEGIN_ID = 'user-input-submit';
var BUTTON_CLEAR_ID = 'user-input-clear';
var BUTTON_RETURN_ID = 'return-to-input';
var BUTTON_ADVANCE_STEP_ID = 'advance-step';
var BUTTON_SOLVE_ALL_ID = 'solve-all';

sudoku.program.setup();

// Button Event Listeners
document.getElementById(BUTTON_BEGIN_ID).addEventListener('click', sudoku.program.enterSolveMode);
document.getElementById(BUTTON_RETURN_ID).addEventListener('click',
    sudoku.program.enterDataInputMode);
document.getElementById(BUTTON_ADVANCE_STEP_ID).addEventListener('click', sudoku.program.next);
document.getElementById(BUTTON_SOLVE_ALL_ID).addEventListener('click', sudoku.program.solveAll);
document.getElementById(BUTTON_CLEAR_ID).addEventListener('click', sudoku.program.clearInputs);

/*
 * Debug functions.
 */
sudoku.grid.drawGrid('debug', 'debug-wrapper');

function debugRowCol(row, col) {
    sudoku.grid.setCellColor('debug', row, col, '#77FF77');
}

function debugClear() {
    for (var i = 0; i < 9; i++) {
        for (var j = 0; j < 9; j++) {
            sudoku.grid.setCellColor('debug', i, j, '#ffffff');
        }
    }
}