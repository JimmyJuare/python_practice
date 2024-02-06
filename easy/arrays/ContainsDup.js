let containsDup = nums => {
    for (let i = 0; i < nums.length; i++) {
        const el = array[i];
        console.log("this is the first el", el);

        for (let j = i + 1; j < nums.length; j++) {
            const secondEl = array[j];
            console.log('this is the second el', secondEl);
            if (el === secondEl) {
                return true
            }

        }
    }
    return false
}

let array = [2, 14, 18, 22, 22]
console.log(containsDup(array));
