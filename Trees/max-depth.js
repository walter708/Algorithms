/*

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

*/ 

var maxDepth = function (root) {
  if(root == null)
    {
      return 0;
    }
   else{
     return 1 + Math.max(maxDepth(root.left), maxDepth(root.right))
   }
};


function TreeNode(val, left = undefined, right = undefined) {
   this.val = (val===undefined ? 0 : val)
  this.left = (left===undefined ? null : left)
   this.right = (right===undefined ? null : right)
}

function Tree(root = undefined ) {

this.root = (root===undefined ? null : root)
}

let root = null;
let treeOne = new Tree(root);



let leafL= new TreeNode(7)
let leafTwo = new TreeNode(15)
let leafOne = new TreeNode(9)
let nodeOneR = new TreeNode(20 , leafTwo , leafL)
let nodeOne = new TreeNode(3 , leafOne , nodeOneR )

treeOne.root = nodeOne;

console.log( maxDepth (treeOne.root) )