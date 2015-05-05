var csvjson = require('csvjson');

//csvjson.toObject('./sample.csv').output

process.argv.forEach(function (val, index, array) {
  console.log(index + ' - ' + val);
});

if(process.argv.indexOf('-i') === -1){
	console.log('No Input File must have -i')
	return 'No Input File must have -i';
}
var input = process.argv[process.argv.indexOf('-i')+1];
console.log('input file',input)


var from = '1987_SIC_to_2002_NAICS.csv';


var concordances = csvjson.toObject('./concordances/'+from).output;
	var conversion = {};

	concordances.forEach(function(convert){
		conversion[convert.SIC] = convert['2002 NAICS'];
	})

console.log('open file','./dataProcessing/raw/'+input)
var file2Convert = csvjson.toObject('./dataProcessing/raw/'+input).output;
console.log(file2Convert[2])

var output = file2Convert.map(function(row){
	row.naics = conversion[row.sic]
});

output.map(function(outrow,i){
	if(i < 20){
		console.log(outrow)
	}
})
