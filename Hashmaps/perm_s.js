function perm_s(s1, s2) {
    let firstMap = {};
    let secondMap = {};
    let r = 0;
    let l = 0;
    let match = 0;
    for (let i = 0; i < 26; i++) {
        firstMap[String.fromCharCode(i + 97)] = 0;
        secondMap[String.fromCharCode(i + 97)] = 0;
    }


    while (r < s1.length) {
        firstMap[s1[r]] += 1;
        secondMap[s2[r]] += 1;
        r += 1;
    }
    for (let j = 0; j < 26; j++) {
        (firstMap[String.fromCharCode(j + 97)] == secondMap[String.fromCharCode(j + 97)]) ? match += 1: match += 0;
    }


    for (r = s1.length; r < s2.length; r++) {

        if (match == 26) {
            return true;
        }


        let index = s2[r];

        secondMap[index] += 1;

        if (secondMap[index] == firstMap[index]) {
            match += 1;
        }
        if (secondMap[index] == (firstMap[index] + 1)) {
            match -= 1;
        }

        let index1 = s2[l];;

        secondMap[index1] -= 1;

        if (secondMap[index1] == firstMap[index1]) {
            match += 1;
        }
        if (secondMap[index1] == (firstMap[index1] - 1)) {
            match -= 1;
        }

        l += 1;
    }

    if (match == 26) {
        return true;
    } else {
        return false;
    }

}

console.log(perm_s("abc", "hbdghgbfdvafc"))