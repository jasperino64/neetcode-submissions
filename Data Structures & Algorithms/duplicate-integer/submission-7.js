class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let d = {}
        for (const x of nums) {
            if (x in d){
                return true
            }
            d[x] = true
        }
        return false
    }
}
