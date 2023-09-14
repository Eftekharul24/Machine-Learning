<!DOCTYPE html>
<html>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<body>
<h1>Using Plotly.js</h1>

<p>X values:<br>
<input id="xvalues" style="width:95%" type="text"
value="50,60,70,80,90,100,110,120,130,140,150"></p>

<p>Y values:<br>
<input id="yvalues" style="width:95%" type="text"
value="7,8,8,9,9,9,10,11,14,14,15"></p>

<button onclick='plot("scatter")'>Scatter</button>
<button onclick='plot("lines")'>Draw Lines</button>

<div id="myPlot" style="width:100%;max-width:700px"></div>

<script>
function plot(type) {
const xArray = document.getElementById("xvalues").value.split(',');
const yArray = document.getElementById("yvalues").value.split(',');
let mode = "lines";
if (type == "scatter") {mode = "markers"}
  Plotly.newPlot("myPlot", [{x:xArray, y:yArray, mode:mode, type:"scatter"}]);
}
</script>

</body>
</html>
