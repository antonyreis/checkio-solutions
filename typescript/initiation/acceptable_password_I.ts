import assert from "assert";

function isAcceptablePassword(password: string): boolean {
    if (password.length > 6) {
        return true;
    } else { return false }
}

console.log("Example:");
console.log(isAcceptablePassword("short"));

// These "asserts" are used for self-checking
assert.strictEqual(isAcceptablePassword("short"), false);
assert.strictEqual(isAcceptablePassword("muchlonger"), true);
assert.strictEqual(isAcceptablePassword("ashort"), false);

console.log("Coding complete? Click 'Check Solution' to earn rewards!");
