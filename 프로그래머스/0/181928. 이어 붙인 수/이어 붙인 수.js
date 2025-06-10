function solution(num_list) {
	const odd = num_list.filter((num) => num % 2 !== 0).join("");
	const even = num_list.filter((num) => num % 2 === 0).join("");

	var answer = Number(odd) + Number(even);
	return answer;
}
