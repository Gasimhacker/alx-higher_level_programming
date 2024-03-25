#!/usr/bin/node
exports.callMeMoby = function (a, theFunction) {
  for (let i = 0; i < a; i++) {
    theFunction();
  }
};
