function renderGraph(payload) {
    let myChart = echarts.init(document.getElementById("main"));

    let { event, reasons, results } = payload;
    
    // original node position
    let xOriginal = 500,
        yOriginal = 500;
    // increment: [x, y]
    // x represents x increment
    // y represents y increment
    let increment = [5, 0.5];

    let data = [].concat(
        { name: event, x: xOriginal, y: yOriginal, value: event },
        paintNode({ x: xOriginal, y: yOriginal }, [-1 * increment[0], increment[1]], reasons),
        paintNode({ x: xOriginal, y: yOriginal }, [increment[0], increment[1]], results)
    );
    let links = [].concat(
        paintEdgeFromSource(event, results),
        paintEdgeToTarget(reasons, event)
    );
    // console.log(links)

    let option = {
        series: [
            {
                type: "graph",
                roam: true,
                label: {
                    show: true
                },
                symbol: "circle",
                symbolSize: [70, 40],
                edgeSymbol: ["circle", "arrow"],
                edgeSymbolSize: [4, 15],
                center: [500, 500],
                lineStyle: {
                    width: 1.5,
                    opacity: 1
                },
                data,
                links
            }
        ]
    };

    myChart.setOption(option);
}

function paintNode(baseNode, increment, values) {
    let { x: xBase, y: yBase } = baseNode;

    return values.map((item, index) => {
        return {
            name: item,
            x: xBase + increment[0],
            y: yBase + index * increment[1],
            value: item
        };
    });
}

function paintEdgeFromSource(source, targets) {
    return targets.map((item) => {
        return {
            source: source,
            target: item
        };
    });
}

function paintEdgeToTarget(sources, target) {
    return sources.map((item) => {
        return {
            source: item,
            target: target
        };
    });
}

export default renderGraph;
