// from data.js
var tableData = data;
console.log(tableData);

// Part 1 ////

var tbody = d3.select("tbody");

data.forEach((UFOsighthings) => {
  var row = tbody.append("tr");
  Object.entries(UFOsighthings).forEach(([key, value]) => {
    console.log(key, value);
    var cell = tbody.append("td");
    cell.text(value);
  });
});


var submit = d3.select("#submit");

// function to take input and recreate table
submit.on("click", function() {
  // stops page from refreshing
  d3.event.preventDefault();

  d3.select(".summary").html("");

  // actual user input as variable
  var inputElement = d3.select("#datetime");
  var inputValue = inputElement.property("value");

  // if the data in the original table matches the user input, add it to the table
  var filteredData = tableData.filter(tableData => tableData.datetime === inputValue);

  // loop to add the "matching data" to visable table
  filteredData.forEach((dateData) => {
    var row = tbody.append("tr");
    Object.entries(dateData).forEach(([key, value]) => {
      var cell = tbody.append("td");
      cell.text(value);
    });
  });
});
// mic drop. im going to bed.