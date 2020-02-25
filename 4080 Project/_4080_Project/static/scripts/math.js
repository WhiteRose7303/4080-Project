var sudoku = sudoku || {};
sudoku.math = sudoku.math || {};

/**
 * Matrix object.
 *
 * @constructor
 * @param initialArgument
 *          The initial value(s) to populate the Matrix. Can either be (a) a
 *          single value or null, (b) a 9x9 array of arrays, or (c) another
 *          matrix object. Default: null.
 * @return matrix A matrix instance.
 */
sudoku.math.Matrix = class extends sudoku.implementation.math.Matrix { };