function solution(num_list) {
	const sum = num_list.reduce((acc, num) => acc + num, 0);
	const mul = num_list.reduce((acc, num) => acc * num, 1);

	if (Math.pow(sum, 2) > mul) return 1;

	return 0;
}
