function getConcatenation(nums: number[]): number[] {
  const n = nums.length;
  const ans = new Array(2 * n);

  for (let i = 0; i <= nums.length; i++) {
    ans[i] = nums[i];
    ans[i + n] = nums[i];
  }

  return ans;
}
