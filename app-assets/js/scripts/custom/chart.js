// // Bar chart
// window.onload = function () {
//   var dataPoints = [];

//   var chart = new CanvasJS.Chart("chartContainer", {
//     animationEnabled: true,
//     theme: "light",
//     title: {
//       text: "피해 등록 현황",
//     },

//     data: [
//       {
//         type: "column",
//         yValueFormatString: "#,### 건",
//         dataPoints: dataPoints,
//       },
//     ],
//   });

//   function addData(data) {
//     for (var i = 0; i < data.length; i++) {
//       dataPoints.push({
//         x: new Date(data[i].date),
//         y: data[i].units,
//       });
//     }
//     chart.render();
//   }

//   $.getJSON(
//     'chart.json',
//     // "https://canvasjs.com/data/gallery/javascript/daily-sales-data.json",
//     addData
//   );
// };
