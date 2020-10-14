import React from 'react';
import ReactApexChart from 'react-apexcharts';


const ChartGenerator = ({ data }) => {
    const buildData = () => {
        let out = {
            categories: [],
            series: []
        }
        Object.keys( data ).forEach((key) => {
            out.categories.push( data[key].time );
            out.series.push( parseFloat(data[key].temperature) );
        })
        return out;
    }
    const chart_data = buildData();
    const chart = {
        options: {
            chart: {
              id: 'Monitor',
              type: 'scatter',
              zoom: {
                  enabled: true,
                  type: 'xy'
              }
            },
            xaxis: {
              categories: chart_data.categories
            }
        },
        title: {
            text: 'RaspBerry',
            align: 'center'
        },
        series: [
          {
            name: "temperatute-1",
            data: chart_data.series
          }
        ]   
    }
    return (
        <ReactApexChart
            options = { chart.options }
            series = { chart.series }
            type = 'scatter'
            height = { 500 }
        />
    )
}
export default ChartGenerator;