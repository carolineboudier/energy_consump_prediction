var gauge = function(container, configuration) {
    var that = {};
    var config = {
        size: 200,
        clipWidth: 200,
        clipHeight: 110,
        ringInset: 20,
        ringWidth: 20,

        pointerWidth: 10,
        pointerTailLength: 5,
        pointerHeadLengthPercent: 0.9,

        minValue: 0,
        maxValue: 500,

        minAngle: -90,
        maxAngle: 90,

        transitionMs: 750,

        majorTicks: 11,
        labelFormat: d3.format(',g'),
        labelInset: 10,

        arcColorFn: [d3.rgb('#66e59d'), d3.rgb('#66e59d'), d3.rgb('#fee08b'), d3.rgb('#fee08b'), d3.rgb('#fee08b'), d3.rgb('#d73027'), d3.rgb('#d73027'), d3.rgb('#d73027'), d3.rgb('#d73027'), d3.rgb('#d73027'), d3.rgb('#d73027')]
        
    };
    var range = undefined;
    var r = undefined;
    var pointerHeadLength = undefined;
    var value = 0;

    var svg = undefined;
    var arc = undefined;
    var scale = undefined;
    var ticks = undefined;
    var tickData = undefined;
    var pointer = undefined;

    var donut = d3.layout.pie();

    function deg2rad(deg) {
        return deg * Math.PI / 180;
    }

    function newAngle(d) {
        var ratio = scale(d);
        var newAngle = config.minAngle + (ratio * range);
        return newAngle;
    }

    function configure(configuration) {
        var prop = undefined;
        for ( prop in configuration ) {
            config[prop] = configuration[prop];
        }

    range = config.maxAngle - config.minAngle;
    r = config.size / 2;
    pointerHeadLength = Math.round(r * config.pointerHeadLengthPercent);

    // a linear scale that maps domain values to a percent from 0..1
    scale = d3.scale.linear()
            .range([0,1])
            .domain([config.minValue, config.maxValue]);

    ticks = scale.ticks(config.majorTicks);
    tickData = d3.range(config.majorTicks).map(function() {return 1/config.majorTicks;});

    arc = d3.svg.arc()
          .innerRadius(r - config.ringWidth - config.ringInset)
          .outerRadius(r - config.ringInset)
          .startAngle(function(d, i) {
                var ratio = d * i;
                return deg2rad(config.minAngle + (ratio * range));
           })
           .endAngle(function(d, i) {
                var ratio = d * (i+1);
                return deg2rad(config.minAngle + (ratio * range));
            });
    }
    that.configure = configure;
    
    function centerTranslation() {
        return 'translate('+r +','+ r +')';
    }

    function isRendered() {
        return (svg !== undefined);
    }
    that.isRendered = isRendered;
    
    function render(newValue) {
        
        svg = d3.select(container)
            .append('svg:svg')
            .attr('id', 'gauge-score')
            .attr('class', 'gauge')
            .attr('width', config.clipWidth)
            .attr('height', config.clipHeight);
        
        var centerTx = centerTranslation();

        var arcs = svg.append('g')
                .attr('class', 'arc')
                .attr('transform', centerTx);

        arcs.selectAll('path')
            .data(tickData)
            .enter().append('path')
            .attr('fill', function(d, i) {return config.arcColorFn[i];})
            .attr('d', arc);

        var lg = svg.append('g')
                .attr('class', 'label')
                .attr('transform', centerTx);
        
        lg.selectAll('text')
            .data(ticks)
            .enter().append('text')
            .attr('transform', function(d) {
                    var ratio = scale(d);
                    var newAngle = config.minAngle + (ratio * range);
                    return 'rotate(' +newAngle +') translate(0,' +(config.labelInset - r) +')';
            })
            .text(config.labelFormat);

         var lineData = [ [config.pointerWidth / 2, 0], 
                        [0, -pointerHeadLength],
                        [-(config.pointerWidth / 2), 0],
                        [0, config.pointerTailLength],
                        [config.pointerWidth / 2, 0] ];
         
         var pointerLine = d3.svg.line().interpolate('monotone');
         var pg = svg.append('g').data([lineData])
                     .attr('class', 'pointer')
                     .attr('transform', centerTx);

         pointer = pg.append('path')
                     .attr('id','gauge-pointer')
                     .attr('d', pointerLine/*function(d) { return pointerLine(d) +'Z';}*/ )
                     .attr('transform', 'rotate(' +config.minAngle +')');

         update(newValue === undefined ? 0 : newValue);
    }
    that.render = render;
    
    function update(newValue, newConfiguration) {
        if ( newConfiguration  !== undefined) {
            configure(newConfiguration);
        }
        var ratio = scale(newValue);
        var newAngle = config.minAngle + (ratio * range);
        
        pointer.transition()
            .duration(config.transitionMs)
            .ease('elastic')
            .attr('transform', 'rotate(' +newAngle +')');
        
    }
    that.update = update;

    configure(configuration);

    return that;
};

function onDocumentReady(val) {
     
    var powerGauge = gauge('#power-gauge', {
        size: 300,
        clipWidth: 300,
        clipHeight: 180,
        ringWidth: 60,
        maxValue: 100,
        transitionMs: 4000,
    });
 
    var legendGauge = document.getElementById('gauge-legend');
    
    flagFirst = (legendGauge.innerHTML === '');
    if (!flagFirst) {
        var mygauge = document.getElementById('gauge-score');
        mygauge.remove();  
    }
        
    powerGauge.render(val);
        
    let legend = "Score = " + val;
    legend = legend.substring(0, 12) + "%";    
    legendGauge.innerHTML = "<i>" + legend + "</i>";    

    
}

/* Function that launches an API Call to the API Node to get the Fraud Result */
function run_scoring(variables) {
  
       var flow_run = $.getJSON(getWebAppBackendUrl('/scoring_api_call')+'/'+JSON.stringify(variables),function(data){
                 /*console.log(JSON.stringify(data));*/
                 R = JSON.parse(JSON.stringify(data));
                 value=R.results
                 /*console.log(R.results);*/

                 /* Refresh the Gauge */
                 onDocumentReady(value);
    
     })
 }


let validationButton = document.getElementById('validation-button');

validationButton.addEventListener('click', function (event) {
    
    let id = document.getElementById('id').value;
    let year_built = document.getElementById('year_built').value;
    let floor_area = document.getElementById('floor_area').value;
    let warehouse_found = document.getElementById('warehouse_found').checked.toString();
    let public_found = document.getElementById('public_found').checked.toString();
    let State_factor = document.getElementById('State_factor').value;
    
    /* Create a variable with parameters to push to the backend */
    variables = {};
    variables['id'] = id;
    variables['year_built'] = year_built;
    variables['floor_area'] = floor_area;
    variables['warehouse_found'] = warehouse_found;
    variables['public_found'] = public_found;
    variables['State_factor'] = State_factor;
    
    run_scoring(variables);
    event.preventDefault();
    });