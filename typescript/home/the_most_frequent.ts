import assert from "assert";

function mostFrequent(data: string[]): string {
    let count = 0;
    let newCount;
    let greater;
    
    data.forEach(str => {
        newCount = data.filter(value => value === str).length;
        if (newCount > count) {
            count = newCount
            greater = str
        }
    })
    return greater;
}

console.log("Example:");
console.log(mostFrequent(["a", "b", "c", "a", "b", "a"]));

// These "asserts" are used for self-checking
assert.strictEqual(mostFrequent(["a", "b", "c", "a", "b", "a"]), "a");
assert.strictEqual(mostFrequent(["a", "a", "bi", "bi", "bi"]), "bi");

console.log("Coding complete? Click 'Check Solution' to earn rewards!");
