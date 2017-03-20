var margin = {top: 40, right: 160, bottom: 35, left: 100};

var width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var svg2 = d3.select("body")
  .append("svg")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
  .append("g")
  .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var data = [
    {
        year: "2016",
        Computerother: "55114",
        Engineer: "19900",
        ComputerProgrammer: "87119",
        SoftwareDeveloper: "110593",
        ComputerSystemAnalyst: "108997",
        DatabaseAdmin: "9000",
        Networks: "13564",
        IT: "8997"
    },
    {
        year: "2015",
        Computerother:" 50114",
        Engineer: "15900",
        ComputerProgrammer: "81119",
        SoftwareDeveloper: "103593",
        ComputerSystemAnalyst: "107997",
        DatabaseAdmin: "7490",
        Networks: "10459",
        IT: "7997"
    },
   {
        year: "2014",
        Computerother: "36228",
        Engineer: "13755",
        ComputerProgrammer: "65027",
        SoftwareDeveloper: "81721",
        ComputerSystemAnalyst: "85080",
        DatabaseAdmin: "6406",
        Networks: "8008",
        IT: "5517"
    },
    {
        year: "2013",
        Computerother: "27497",
        Engineer: "12017",
        ComputerProgrammer: "51220",
        SoftwareDeveloper: "61667",
        ComputerSystemAnalyst: "77415",
        DatabaseAdmin: "4715",
        Networks: "5958",
        IT: "6802"
    },
    {
        year: "2012",
        Computerother: "20514",
        Engineer: "11785",
        ComputerProgrammer: "46571",
        SoftwareDeveloper: "54405",
        ComputerSystemAnalyst: "61448",
        DatabaseAdmin: "4228",
        Networks:" 5577",
        IT: "6954"
    }
];


var parse = d3.time.format("%Y").parse;

var dataset = d3.layout.stack()(["IT", "Networks", "DatabaseAdmin", "ComputerSystemAnalyst", "SoftwareDeveloper", "ComputerProgrammer", "Engineer", "Computerother"].map(function(fruit) {
  return data.map(function(d) {
    return {x: parse(d.year), y: +d[fruit]};
  });
}));

var x = d3.scale.ordinal()
  .domain(dataset[0].map(function(d) { return d.x; }))
  .rangeRoundBands([10, width-10], 0.02);

var y = d3.scale.linear()
  .domain([0, d3.max(dataset, function(d) {  return d3.max(d, function(d) { return d.y0 + d.y; });  })])
    .range([height, 0]);
var colors = ["#581845", "#800000" , "b33040", "#d25c4d", "#ff8c00", "#f2b447",  "#d9d574", "#D8BFD8"];

var yAxis = d3.svg.axis()
  .scale(y)
  .orient("left")
  .ticks(5)
  .tickSize(-width, 0, 0)
  .tickFormat( function(d) { return d } );

var xAxis = d3.svg.axis()
  .scale(x)
  .orient("bottom")
  .tickFormat(d3.time.format("%Y"));

svg2.append("g")
  .attr("class", "y axis")
  .call(yAxis);

svg2.append("g")
  .attr("class", "x axis")
  .attr("transform", "translate(0," + height + ")")
  .call(xAxis);

var groups = svg2.selectAll("g.cost")
  .data(dataset)
  .enter().append("g")
  .attr("class", "cost")
  .style("fill", function(d, i) { return colors[i]; });

var rect = groups.selectAll("rect")
  .data(function(d) { return d; })
  .enter()
  .append("rect")
  .attr("x", function(d) { return x(d.x); })
  .attr("y", function(d) { return y(d.y0 + d.y); })
  .attr("height", function(d) { return y(d.y0) - y(d.y0 + d.y); })
  .attr("width", x.rangeBand())
  .on("mouseover", function() { tooltip.style("display", null); })
  .on("mouseout", function() { tooltip.style("display", "none"); })
  .on("mousemove", function(d) {
    var xPosition = d3.mouse(this)[0] - 15;
    var yPosition = d3.mouse(this)[1] - 25;
    tooltip.attr("transform", "translate(" + xPosition + "," + yPosition + ")");
    tooltip.select("text").text(d.y);
  });

var legend = svg2.selectAll(".legend")
  .data(colors)
  .enter().append("g")
  .attr("class", "legend")
  .attr("transform", function(d, i) { return "translate(30," + i * 19 + ")"; });
 
legend.append("rect")
  .attr("x", width - 18)
  .attr("width", 18)
  .attr("height", 18)
  .style("fill", function(d, i) {return colors.slice().reverse()[i];});
 
legend.append("text")
  .attr("x", width + 5)
  .attr("y", 9)
  .attr("dy", ".35em")
  .style("text-anchor", "start")
  .text(function(d, i) { 
    switch (i) {
      case 0: return "Computer Other";
      case 1: return "Engineer";
      case 2: return "Computer Programmer";
      case 3: return "Software Developer";
      case 4: return "Computer System Analyst";
      case 5: return "Database Administrator";
      case 6: return "Networks";
      case 7: return "IT";
    }
  });

var tooltip = svg2.append("g")
  .attr("class", "tooltip")
  .style("display", "none");
    
tooltip.append("rect")
  .attr("width", 30)
  .attr("height", 20)
  .attr("fill", "white")
  .style("opacity", 0.5);

tooltip.append("text")
  .attr("x", 15)
  .attr("dy", "1.2em")
  .style("text-anchor", "middle")
  .attr("font-size", "12px")
  .attr("font-weight", "bold");

