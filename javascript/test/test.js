const { expect } = require('chai');
const { isMatch } = require('../leetcode');
const { Human, Male } = require('../web/inheritance');

describe('LeetCode', () => {
    describe('@isMatch', () => {
        it('should return true if regexp matches', () => {
            expect(isMatch("aa", "a")).to.be.false;
            expect(isMatch("aa", "aa")).to.be.true;
            expect(isMatch("aaa", "aa")).to.be.false;
            expect(isMatch("aa", "a*")).to.be.true;
            expect(isMatch("aa", ".*")).to.be.true;
            expect(isMatch("ab", ".*")).to.be.true;
            expect(isMatch("aab", "c*a*b")).to.be.true;
        });
    });

});

describe('Inheritance', () => {
    it('should be awesome', () => {
        let h = new Human('alex');
        let m = new Male('Paul');
        console.log(h, m)
        expect(h._tick).to.be.equal(0)
        expect(m._tick).to.be.equal(0)
    });
})

