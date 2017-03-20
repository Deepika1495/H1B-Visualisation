var win_w = $( window ).width()*0.9;
var win_h = $( window ).height()*0.9;

var margin = {top: 60, right: 10, bottom: 10, left: 10},
    width = win_w - margin.left - margin.right,
    height = win_h - margin.top - margin.bottom;
	
var l_width = 200 - margin.left;
var l_height = margin.top - (margin.left*2);

var values = d3.range(l_width);	

//var color2 = d3.scale.linear()
  //  .range(["rgb(0,155,255)","rgb(150,150,150)","rgb(255,100,0)"])
//	.interpolate(d3.interpolateRgb)
//	.domain([0, (values.length - 1)/2, values.length - 1]);	

var color = d3.scale.ordinal()
    .domain(["foo", "bar", "baz"])
    .range(["#eff3ff","#c6dbef","#9ecae1","#6baed6","#4292c6","#2171b5","#084594"]);

//var x = d3.scale.ordinal()
  //.domain(values)
  //.rangeRoundBands([0, l_width]);
  
var svg1 = d3.select("body").append("svg")
    .attr("id","treemap");

var g =svg1.append("g").attr("transform", function(d) { return "translate(" + margin.left + "," + margin.left + ")"; });  

//var tree_path = "year12.json";
//var tree_path2 = "year15.json";
//var tree_path3 = "year14.json";
//var tree_path4 = "year13.json";
//var tree_path5 = "year12.json";

var div = d3.select("body").append("div")
    .attr("id", "chart") 
    .attr("class", "chart") 
    .style("width", (width + margin.left + margin.right) + "px")
    .style("height", (height + margin.top + margin.bottom) + "px")
    .style("left", margin.left + "px")
    .style("top", margin.top + "px");

var active_year;

render("year16.json");

$("input").change(function(){
  active_year = $("input[name='mode']:checked").val();
}).change(function(){
  render(active_year+".json");
});


function render(map){
  var treemap = d3.layout.treemap()
      .size([width, height])
      .sticky(true)
      .mode("slice-dice")
      .sort(function(d) { return d.order; });  

  $.getJSON(map, function(root) {
    var this_tree = treemap.value(function(d) { return d.size;}).nodes(root);
    this_tree.forEach(function(d) { d.real_size=d.dx * d.dy;});
    
    var node = div.selectAll(".node")
	.data(this_tree)
	.enter().append("div")
	.attr("class", "node")
	.attr("id", function(d){ return d.id;})
	.call(position)
	.text(function(d) { return d.children ? null : d.name; });
    
    var value = function(d) { return d.size; }
    var that_tree = treemap.value(value).nodes(root).map(function(d) { return (d.dx * d.dy)/d.real_size; });
    color2.domain([d3.min(that_tree), 1, d3.max(that_tree)]);	
    animate(treemap, node, value);
  });
}

var animate = function(treemap, node, value){
  node.data(treemap.value(value).nodes)
    .transition()
    .duration(1500)
    .call(position);
}

function position() {
  this.style("left", function(d) { return d.x + "px"; })
    .style("top", function(d) { return d.y + "px"; })
    .style("width", function(d) { return Math.max(0, d.dx - 1) + "px"; })
    .style("height", function(d) { return Math.max(0, d.dy - 1) + "px"; })
    .style("background",function(d) { return color(d.name);});
}
