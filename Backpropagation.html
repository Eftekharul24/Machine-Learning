<!DOCTYPE html>
<html>
<script src="myperceptron.js"></script>
<script src="myplotlib.js"></script>
<body>
<canvas id="myCanvas" width="400px" height="400px" style="width:100%;max-width:400px;border:1px solid black"></canvas>

<script>
// Initiate Values
const numPoints = 500;
const learningRate = 0.00001;

// Create a Plotter
const plotter = new XYPlotter("myCanvas");
plotter.transformXY();
const xMax = plotter.xMax;
const yMax = plotter.yMax;
const xMin = plotter.xMin;
const yMin = plotter.yMin;

// Create Random XY Points
const xPoints = [];
const yPoints = [];
for (let i = 0; i < numPoints; i++) {
  xPoints[i] = Math.random() * xMax;
  yPoints[i] = Math.random() * yMax;
}

// Line Function
function f(x) {
  return x * 1.2 + 50;
}

//Plot the Line
plotter.plotLine(xMin, f(xMin), xMax, f(xMax), "black");

// Compute Desired Answers
const desired = [];
for (let i = 0; i < numPoints; i++) {
  desired[i] = 0;
  if (yPoints[i] > f(xPoints[i])) {desired[i] = 1}
}

// Create a Perceptron
const ptron = new Perceptron(2, learningRate);

// Train the Perceptron
for (let j = 0; j <= 10000; j++) {
  for (let i = 0; i < numPoints; i++) {
    ptron.train([xPoints[i], yPoints[i]], desired[i]);
  }
}

// Display the Result
for (let i = 0; i < numPoints; i++) {
  const x = xPoints[i];
  const y = yPoints[i];
  let guess = ptron.activate([x, y, ptron.bias]);
  let color = "black";
  if (guess == 0) color = "blue";
  plotter.plotPoint(x, y, color);
}
</script>
</body>
</html>
