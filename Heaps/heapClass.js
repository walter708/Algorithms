class BinHeap {
  constructor() {
    this.value = [100, 50, 10, 20, 30, 5, 2];
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

  extractMax() {
    const len = this.value.length - 1;
    [this.value[0], this.value[len]] = [this.value[len], this.value[0]];
    const root = this.value.pop();
    this.bubbleDown();
    return root;
  }

  bubbleDown() {
    let smallest = 0;
    let len = this.value.length;
    let left;
    let right;
    while (smallest < len) {
      left = 2 * smallest + 1;
      right = 2 * smallest + 2;
      let index = this.findMaxIndex(left, right);
      if (index === Infinity) break;
      if (this.value[smallest] > this.value[index]) break;
      [this.value[smallest], this.value[index]] = [
        this.value[index],
        this.value[smallest],
      ];
      smallest = index;
    }
  }

  findMaxIndex(idxA, idxB) {
    const len = this.value.length;
    if (idxA < len && idxB < len) {
      if (this.value[idxA] > this.value[idxB]) {
        return idxA;
      } else {
        return idxB;
      }
    } else if (idxA >= len && idxB >= len) {
      return Infinity;
    } else if (idxB >= len) {
      return idxA;
    } else {
      return idxB;
    }
  }
}

let h = new BinHeap();
//
// [100, 50, 10, 20, 30, 5, 2]
// [2, 50, 10 , 20, 30, 5]
// [50, 2, 10, 20, 30, 5]
// [50, 30, 10, 20, 2, 5]
