'''
You are given two strings: pattern and source. The first string pattern contains only the symbols 0 and 1, and the second string source contains only lowercase English letters.

Your task is to calculate the number of substrings of source that match pattern. 

We’ll say that a substring source[l..r] matches pattern if the following three conditions are met:
– The pattern and substring are equal in length.
– Where there is a 0 in the pattern, there is a vowel in the substring. 
– Where there is a 1 in the pattern, there is a consonant in the substring. 

Vowels are ‘a‘, ‘e‘, ‘i‘, ‘o‘, ‘u‘, and ‘y‘. All other letters are consonants.

Example

For pattern = "010" and source = "amazing", the output should be solution(pattern, source) = 2.
– “010” matches source[0..2] = "ama". The pattern specifies “vowel, consonant, vowel”. “ama” matches this pattern: 0 matches a, 1 matches m, and 0 matches a. 
– “010” doesn’t match source[1..3] = "maz" 
– “010” matches source[2..4] = "azi" 
– “010” doesn’t match source[3..5] = "zin" 
– “010” doesn’t match source[4..6] = "ing"

So, there are 2 matches. For a visual demonstration, see the example video. 

For pattern = "100" and source = "codesignal", the output should be solution(pattern, source) = 0.
– There are no double vowels in the string "codesignal", so it’s not possible for any of its substrings to match this pattern.

Guaranteed constraints:
1 ≤ source.length ≤ 103
1 ≤ pattern.length ≤ 103
'''

vowels = ['a', 'e', 'i', 'o', 'u', 'y'] 

def check_match(source, pattern, check):
    for i in range(len(pattern)):
        if pattern[i]=='0':
            if source[i+check] not in vowels:
                return 0
        else:
            if source[i+check] in vowels:
                return 0
    return 1


def solution(source, pattern):
    answer = 0
    for check in range(len(source)-len(pattern)+1):
        answer += check_match(source, pattern, check)
    return answer

pattern = "010"
source = "amazing"
print(solution(source, pattern)) # 2

pattern = "100"
source = "codesignal"
print(solution(source, pattern)) # 0
