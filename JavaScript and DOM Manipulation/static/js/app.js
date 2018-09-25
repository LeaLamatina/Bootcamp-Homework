// creating variables for the input data and the button
var tableData = d3.select("tbody");

// adds the data file into the document
data.forEach((ufoSighting) => {
  var row = tableData.append("tr");
  Object.entries(ufoSighting).forEach(([key, value]) => {
    var cell = tableData.append("td");
    cell.text(value);
  });
});