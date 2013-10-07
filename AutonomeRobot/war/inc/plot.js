// parameters
graph = new Object();
// type to functions
graph.funcs = new Array();
graph.funcs["pie"] = new Array("Taart","pie");
graph.funcs["text"] = new Array("Tekst","text");
graph.funcs["prog"] = new Array("Progress","prog");
graph.funcs["bar"] = new Array("Staaf","bar");
// type handlers
function scatter(data,options){
	$("#"+graph.graphDivID).html("");
	$.jqplot(graph.graphDivID, data);
}
function text(data,options){
	$("#"+graph.graphDivID).html("");
	$("#"+graph.graphDivID).html(data[0]);
}
function pie(data,options){
	$("#"+graph.graphDivID).html("");
	if(data.length==0){
		$("#"+graph.graphDivID).html("Geen data");
		return;
	}
	$.jqplot(graph.graphDivID, [data],
		{
		  seriesDefaults: {
			// Make this a pie chart.
			renderer: jQuery.jqplot.PieRenderer,
			rendererOptions: {
			  // Put data labels on the pie slices.
			  // By default, labels show the percentage of the slice.
			  showDataLabels: true
			}
		  },
		  legend: { show:true, location: 'e' }
		}
	 );
}
function bar(data,options){
	$("#"+graph.graphDivID).html("");
	var values = data[0];
    // Can specify a custom tick Array.
    // Ticks should match up one for each y value (category) in the series.
    var ticks = data[1];
    if(!options.xlabel)
    	options.xlabel = "";
    if(!options.ylabel)
    	options.ylabel = "";
    var plot1 = $.jqplot(graph.graphDivID, [values], {
        // The "seriesDefaults" option is an options object that will
        // be applied to all series in the chart.
        seriesDefaults:{
            renderer:$.jqplot.BarRenderer,
            rendererOptions: {fillToZero: true,barDirection:"horizontal"}
        },
        axes: {
            // Use a category axis on the x axis and use our custom ticks.
            yaxis: {
                renderer: $.jqplot.CategoryAxisRenderer,
                ticks: ticks,
                label: options.ylabel
            },
            // Pad the y axis just a little so bars can get close to, but
            // not touch, the grid boundaries.  1.2 is the default padding.
            xaxis: {
                pad: 1.05,
                label: options.xlabel
                //tickOptions: {formatString: '%d%d%d'}
            }
        }
    });
}
function prog(data,options){
	pValue = data[0]*100;
	$("#"+graph.graphDivID).html("<p id='progBar'></p>");
	$("#progBar").progressbar({ max: 100});
	$("#progBar").progressbar({ value: pValue});
}

function getData(jsonURL,catB,graphB,divD,pageID,descB){
	graph.catButton = catB;
	graph.graphButton = graphB;
	graph.graphDivID = divD;
	graph.descID = descB;
	$("#"+graph.graphDivID).html("Please wait, statistics are being fetched...");
	$.getJSON(jsonURL,function(json){
		//graph methods and properties
		graph.count = 0;
		graph.cats = json;
		graph.getCat = function(){
			return this.cats[this.count];
		};
		graph.nextCat = function(){
			this.count++;
			if(this.count==this.cats.length) this.count=0;
			return this.cats[this.count];
		};
		for(i=0;i<graph.cats.length;i++){
			//cat methods and properties
			graph.cats[i].count = 0;
			graph.cats[i].getData = function(){
				return this.data[this.count];
			};
			graph.cats[i].nextData = function(){
				this.count++;
				if(this.count==this.data.length) this.count = 0;
				return this.data[this.count];
			};
		}
		$("div#"+pageID).find("div[name='preLoadWrap']").slideUp(function(){
			$("div#"+pageID).find("div[name='loadWrap']").slideDown();
			drawGraph();
		});
	});
}
function drawGraph(){
	$(graph.catButton).text(graph.getCat().name);
	$("#"+graph.descID).text(graph.getCat().desc);
	var curData = window.graph.getCat().getData();
	var curCat = window.graph.getCat();
	var type = curCat.type;
	if(curData.name=="")
		$(graph.graphButton).parent().parent().hide();
	else
		$(graph.graphButton).text(curData.name).parent().parent().show();
	eval(graph.funcs[type][1]+"(curData.data,curCat.options)");
}

function changeCat(){
	newCat = window.graph.nextCat();
	$(graph.catButton).text(newCat.name);
	$("#"+graph.descID).text(newCat.desc);
	drawGraph();
}

function changeGraph(){
	var nextGraph = window.graph.getCat().nextData();
	drawGraph();
}