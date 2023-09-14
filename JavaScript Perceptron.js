<!DOCTYPE html>
<html>
<body>
<h1>JavaScript Perceptron</h1>

<p>Will I go to the consert?</p>
<div id="demo"></div>

<script>
const threshold = 1.5;
const inputs = [1, 0, 1, 0, 1];
const weights = [0.7, 0.6, 0.5, 0.3, 0.4];

let sum = 0;
for (let i = 0; i < inputs.length; i++) {
  sum += inputs[i] * weights[i];
}

document.getElementById("demo").innerHTML = (sum > threshold);  
</script>

</body>
</html>
