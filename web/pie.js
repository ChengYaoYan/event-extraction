var myChart = echarts.init(document.getElementById('main'));

let option = {
    backgroundColor: '#2c343c',
    visualMap: {
        show: false,
        min: 80,
        max: 600,
        inRange: {
            colorLightness: [0, 1]
        }
    },
    series: [
        {
            name: 'Reference Page',
            type: 'pie',
            radius: '55%',
            data: [
                {value:400, name:'Searching Engine'},
                {value:335, name:'Direct'},
                {value:310, name:'Email'},
                {value:274, name:'Alliance Advertisement'},
                {value:235, name:'Video Advertisement'}
            ],
            roseType: 'angle',
            itemStyle: {
                shadowBlur: 200,
                shadowColor: 'rgba(0, 0, 0, 0.3)',
                shadowOffsetX: 0,
                shadowOffsetY: 0,
                color: '#c23531',
            },
            label: {
                textStyle: {
                    color: 'rgba(255, 255, 255, 0.5)'
                }
            },
            labelLine: {
                lineStyle: {
                  color: 'rgba(255, 255, 255, 0.5)'
                }
            }
        }
    ]
}

myChart.setOption(option)
