def reverseParentheses(s):
    for i in range(len(s)):
        if s[i] == "(":
            start = i
        if s[i] == ")":
            end = i
            return reverseParentheses(s[:start] + s[start+1:end][::-1] + s[end+1:])
    return s