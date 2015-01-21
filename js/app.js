(function(){
	var app = angular.module('app', []);

	app.rows = [];
	for(let i = 0; i < 4; i++){
		let row = [];
		for(let j = 0; j < 4; j++){
			row.push({});
		}
		app.rows.push(row);
	}
})()