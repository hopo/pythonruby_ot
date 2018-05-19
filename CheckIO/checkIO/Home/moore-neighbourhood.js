"use strict";

function countNeighbours(data, row, col) {
  var topl, topc, topr, bdyl, bdyr, botl, botc, botr;
  if(row == 0) {
    topl = 0, topc = 0, topr = 0
  } else {
    topl = data[row-1][col-1] == undefined ? 0 : data[row-1][col-1];
    topc = data[row-1][col] == undefined ? 0 : data[row-1][col];
    topr = data[row-1][col+1] == undefined ? 0 : data[row-1][col+1];
  } 

  bdyl = data[row][col-1] == undefined ? 0 : data[row][col-1];
  bdyr = data[row][col+1] == undefined ? 0 : data[row][col+1];

  if(row == data.length-1){
    botl = 0, botc = 0, botr = 0;
  } else {
    botl = data[row+1][col-1] == undefined ? 0 : data[row+1][col-1];
    botc = data[row+1][col] == undefined ? 0 : data[row+1][col];
    botr = data[row+1][col+1] == undefined ? 0 : data[row+1][col+1];
  }

  var rslt = topl+topc+topr+bdyl+bdyr+botl+botc+botr;
  return rslt;
}

var assert = require('assert');

if (!global.is_checking) {
    assert.equal(countNeighbours([[1, 0, 0, 1, 0],
                                  [0, 1, 0, 0, 0],
                                  [0, 0, 1, 0, 1],
                                  [1, 0, 0, 0, 0],
                                  [0, 0, 1, 0, 0]], 1, 2), 3, "1st example");

    assert.equal(countNeighbours([[1, 0, 0, 1, 0],
                                  [0, 1, 0, 0, 0],
                                  [0, 0, 1, 0, 1],
                                  [1, 0, 0, 0, 0],
                                  [0, 0, 1, 0, 0]], 0, 0), 1, "2nd example");

    assert.equal(countNeighbours([[1, 1, 1],
                                  [1, 1, 1],
                                  [1, 1, 1]], 0, 2), 3, "Dense corner");

    assert.equal(countNeighbours([[0, 0, 0],
                                  [0, 1, 0],
                                  [0, 0, 0]], 1, 1), 0, "Single");

    console.log("Coding complete? Click 'Check' to review your tests and earn cool rewards!");
}
