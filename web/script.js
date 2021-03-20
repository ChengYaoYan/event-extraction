var myChart = echarts.init(document.getElementById('main'), 'dark');

let option = {
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
        }
    ]
}
myChart.setOption(option)
