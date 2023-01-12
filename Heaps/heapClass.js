class BinHeap {
  constructor() {
    this.value = [];
  }
  insert(item) {
    this.value.push(item);
    const len = this.value.length - 1;
    this.bubbleUp(len);
  }

  bubbleUp(len) {
    let ptr = len;
    let flag = false;
    while (!flag && ptr > 0) {
      let p = Math.floor((ptr - 1) / 2);
      if (this.value[ptr] > this.value[p]) {
        [this.value[ptr], this.value[p]] = [this.value[p], this.value[ptr]];
        ptr = p;
      } else {
        flag = true;
      }
    }
  }
}
