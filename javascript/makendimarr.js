function Ticker(dimList) {
  this._capList = [...dimList];
  this.currentTick = [...dimList];
}

Ticker.prototype.tick = function () {
  if (this.isDone()) return this;
  for (let x = this.currentTick.length-1; x>=0;x--){
    if (this.currentTick[x] !== 0) {
      this.currentTick[x]-=1;
      break;
    } else {
      this.currentTick[x] = this._capList[x];
    }
  }
  return this;
}
Ticker.prototype.isDone = function () {
  for (let x = 0; x < this.currentTick.length; x++) {
    if (this.currentTick[x] !== 0) {
      return false;
    }
  }
  return true;
}
Ticker.prototype.reset = function () {
  this.currentTick = this._capList;
}

module.exports = {
  Ticker: Ticker
}

ndarr = function(){
  return new Array(arguments[0]||0)
    .fill(0)
    .map(ndarr.bind.apply(ndarr, arguments));
}

