<!DOCTYPE html>
<html>
<script src="//unpkg.com/brain.js"></script>
<body>
<h1>Deep Learning with brain.js</h1>
<div id="demo"></div>

<script>
// Create a Neural Network
const network = new brain.NeuralNetwork();

// Train the Network with 4 input objects
network.train([
  {input:[0,0], output:{zero:1}},
  {input:[0,1], output:{one:1}},
  {input:[1,0], output:{one:1}},
  {input:[1,1], output:{zero:1}},
]);

// What is the expected output of [1,0]?
let result = network.run([1,0]);

// Display the probability for "zero" and "one"
document.getElementById("demo").innerHTML =
"one: " + result["one"] + "<br>" + "zero: " + result["zero"];
</script>
</body>
</html>
