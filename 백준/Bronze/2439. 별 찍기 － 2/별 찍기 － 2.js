function solve(n) {
	//     *
	//    **
	//   ***

	let str = "";

	for (let i = 0; i < n; i++) {
		for (let j = i + 1; j < n; j++) {
			str += " ";
		}

		for (let k = 0; k <= i; k++) {
			str += "*";
		}

		if (i !== n - 1) {
			str += "\n";
		}
	}

	console.log(str);
}

// 데이터 입력/출력 부분
const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout,
});

let inputs = [];
rl.on("line", (line) => {
	inputs.push(line);
	if (inputs.length === 1) {
		rl.close();
	}
});

rl.on("close", () => {
	const input = JSON.parse(inputs[0]);
	const answer = solve(input);

	rl.close();
});
