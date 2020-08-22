# My-Leetcode
## Note

### 回溯法

- 回溯法：

  - 通过不停的选择，撤销选择，来穷尽所有可能性，最后将满足条件的结果全部返回
  - 是DFS的一种，实际上就是先序遍历
  - 是一种纯暴力搜索算法，时间复杂度一般是O(N!)
  - 模板：

  ```python
  result = []
  func backtrack(选择列表,路径):
      if 满足结束条件:
          result.add(路径)
          return
      for 选择 in 选择列表:
          做选择
          backtrack(选择列表,路径)
          撤销选择
  ```



