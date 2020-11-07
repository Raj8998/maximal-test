def lengthOfLongestSubstring(s: str) -> int:
    dic, res, start = {}, 0, 0
    for i, ch in enumerate(s):
        if ch in dic:
            res = max(res, i-start)
            start = max(start, dic[ch] +1)
        dic[ch] = i
    return max(res, len(s)-start)

def testFunction():
    string = input("Input: ")
    print("Test case: "+string,"Solution: "+str(lengthOfLongestSubstring(string)),sep="\n" )

if __name__ == '__main__':
    testFunction()
