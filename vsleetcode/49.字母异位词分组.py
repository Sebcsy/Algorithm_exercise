#
# @lc app=leetcode.cn id=49 lang=python
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict={}
        for i in strs:
            key=tuple(sorted(i))
            # 注意字典的key值必须是可以hash的变量类型，所以所有python自带类型中，除了list、dict、set和内部至少带有上述三种类型之一的tuple之外，其余的对象都能当key。
            dict[key] = dict.get(key,[])+[i]
        
        '''python3 字典 values() 方法返回一个视图对象。

dict.keys()、dict.values() 和 dict.items() 返回的都是视图对象（ view objects），提供了字典实体的动态视图，这就意味着字典改变，视图也会跟着变化。

视图对象不是列表，不支持索引，可以使用 list() 来转换为列表。

我们不能对视图对象进行任何的修改，因为字典的视图对象都是只读的。'''

        return list(dict.values())
# @lc code=end
