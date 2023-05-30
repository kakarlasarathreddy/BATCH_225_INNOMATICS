class Leetcode:
        
    # leetcode_771_Assan
    def lc_771(self,jewels,stones):
    
        '''
        You're given strings jewels representing the types of stones that are jewels, and stones representing 
        the stones you have. Each character in stones is a type of stone you have. 
        You want to know how many of the stones you have are also jewels.
        Letters are case sensitive, so "a" is considered a different type of stone from "A".
        
        EXAMPLE:
        Input: jewels = "aA", stones = "aAAbbbb"
        Output: 3
        ----------------------------------------->Assan
        '''

        count =0
        for stone in stones:
            if stone in jewels:
                count+=1
        return count
    
    # leetcode_1748_Assan
    def lc_1748(self,nums):
    
        '''
        You are given an integer array nums. The unique elements of an array are the elements
        that appear exactly once in the array. Return the sum of all the unique elements of nums.
        
        Input: nums = [1,2,3,2]
        Output: 4
        Explanation: The unique elements are [1,3], and the sum is 4.
        ----------------------------------------->Assan
        '''

        x = [i for i in nums if nums.count(i) ==1]
        y = sum(x)
        return y
    
    #leetcode_2138_Assan
    def lc_2138(self,string,k):
    
        '''
        A string s can be partitioned into groups of size k using the following procedure:
        The first group consists of the first k characters of the string, the second group consists of 
        the next k characters of the string,and so on. Each character can be a part of exactly one group.
        For the last group, if the string does not have k characters remaining, a character fill is used to complete the group.
        Note that the partition is done so that after removing the fill character from the last group (if it exists) 
        and concatenating all the groups in order, the resultant string should be s.
        Given the string s, the size of each group k and the character fill, return a string array denoting 
        the composition of every group s has been divided into, using the above procedure.
 
        EXAMPLE:
        Input: s = "abcdefghi", k = 3, fill = "x"
        Output: ["abc","def","ghi"]
        Explanation:
        The first 3 characters "abc" form the first group.
        The next 3 characters "def" form the second group.
        The last 3 characters "ghi" form the third group.
        Since all groups can be completely filled by characters from the string, we do not need to use fill.
        Thus, the groups formed are "abc", "def", and "ghi".
        ----------------------------------------->Assan
        '''

        a=['']
        fill='x'
        for i in string:
            if len(a[-1])<k:
                a[-1] += i

            else:
                a.append('')
                a[-1] +=i
        while len(a[-1]) < k:
            a[-1] += fill
        return a 
    
    #leetcode_2648_Assan
    def lc_2648(self,n):
        
        '''
        Write a generator function that returns a generator object which yields the fibonacci sequence.
        The fibonacci sequence is defined by the relation Xn = Xn-1 + Xn-2.
        The first few numbers of the series are 0, 1, 1, 2, 3, 5, 8, 13.
        
        EXAMPLE:
        Input: callCount = 5
        Output: 0,1,1,2,3
        Explanation:
        const gen = fibGenerator();
        gen.next().value; // 0
        gen.next().value; // 1
        gen.next().value; // 1
        gen.next().value; // 2
        gen.next().value; // 3
        ----------------------------------------->Assan
        '''

        fib_list = []
        a, b = 0, 1
        for _ in range(n):
            fib_list.append(a)
            a, b = b, a + b
        return fib_list
    
    #leetcode_1816_Assan
    def lc_1816(self,string,k):
    
        '''
        A sentence is a list of words that are separated by a single space with no leading or trailing spaces. 
        Each of the words consists of only uppercase and lowercase English letters (no punctuation).
        For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
        You are given a sentence sand an integer k. You want to truncate s such that it contains only the first k words. 
        Return s after truncating it.
        
        EXAMPLE:
        Input: s = "Hello how are you Contestant", k = 4
        Output: "Hello how are you"
        Explanation:
        The words in s are ["Hello", "how" "are", "you", "Contestant"].
        The first 4 words are ["Hello", "how", "are", "you"].
        Hence, you should return "Hello how are you".
        ----------------------------------------->Assan
        '''

        a = string.split()

        b = []

        for i in range(k):
            if len(a)>k:
                b.append(a[i])

                e=' '.join(b)
            else:

                return s
        return e

    # leetcode_1832_Assan
    def lc_1832(self,string):
    
        '''
        A pangram is a sentence where every letter of the English alphabet appears at least once.
        Given a string sentence containing only lowercase English letters, return true if sentence is a pangram,
        or false otherwise.
        
        EXAMPLE:
        Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
        Output: true
        Explanation: sentence contains at least one of every letter of the English alphabet.
        ----------------------------------------->Assan
        '''

        return set(string.lower()) == set('abcdefghijklmnopqrstuvwxyz')
    
    # leetcode_2544_Assan
    def lc_2544(self,n):
    
        '''
        You are given a positive integer n. Each digit of n has a sign according to the following rules:
        The most significant digit is assigned a positive sign.
        Each other digit has an opposite sign to its adjacent digits.
        Return the sum of all digits with their corresponding sign.
        
        EXAMPLE:
        Input: n = 521
        Output: 4
        Explanation: (+5) + (-2) + (+1) = 4.
        ----------------------------------------->Assan
        '''

        sign=1
        result=0
        for i in str(n):
            result+=sign*int(i)
            sign*=-1
        return result
    
    # leetcode_2239_Assan
    def lc_2239(self,nums):
    
        '''
        Given an integer array nums of size n, return the number with the value closest to 0 in nums.
        If there are multiple answers, return the number with the largest value.
        
        EXAMPLE:
        Input: nums = [-4,-2,1,4,8]
        Output: 1
        Explanation:
        The distance from -4 to 0 is |-4| = 4.
        The distance from -2 to 0 is |-2| = 2.
        The distance from 1 to 0 is |1| = 1.
        The distance from 4 to 0 is |4| = 4.
        The distance from 8 to 0 is |8| = 8.
        Thus, the closest number to 0 in the array is 1.
        ----------------------------------------->Assan
        '''

        a=[abs(nums[i]-0) for i in range(len(nums))]

        return min(a)
    
    # leetcode_2243_Assan
    def fun(self, s):
        '''
        You are given a string s consisting of digits and an integer k.
        A round can be completed if the length of s is greater than k. In one round, do the following:
        Divide s into consecutive groups of size k such that the first k characters are in the first group,
        the next k characters are in the second group, and so on. Note that the size of the last group can be smaller than k.
        Replace each group of s with a string representing the sum of all its digits.
        For example, "346" is replaced with "13" because 3 + 4 + 6 = 13.
        Merge consecutive groups together to form a new string. If the length of the string is greater than k,
        repeat from step 1.Return s after all rounds have been completed.

        EXAMPLE:
        Input: s = "11111222223", k = 3
        Output: "135"
        Explanation: 
        - For the first round, we divide s into groups of size 3: "111", "112", "222", and "23".
          ​​​​​Then we calculate the digit sum of each group: 1 + 1 + 1 = 3, 1 + 1 + 2 = 4, 2 + 2 + 2 = 6, and 2 + 3 = 5. 
          So, s becomes "3" + "4" + "6" + "5" = "3465" after the first round.
        - For the second round, we divide s into "346" and "5".
          Then we calculate the digit sum of each group: 3 + 4 + 6 = 13, 5 = 5. 
          So, s becomes "13" + "5" = "135" after second round. 
        Now, s.length <= k, so we return "135" as the answer.
        ----------------------------------------->Assan
        '''
        
        
        return sum(int(digit) for digit in s)

    def lc_2243(self, s, k):
        while len(s) > k:
            groups = [s[i:i+k] for i in range(0, len(s), k)]
            s = ''.join(str(self.fun(group)) for group in groups)
        return s



    def lc_1119(self,x,y):
    
        '''
        Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
        
        EXAMPLE:
        Input: “leetcodeisacommunityforcoders”
        Output: “ltcdscmmntyfrcdrs”
        '''

        return ''.join(str(a) for a in x.lower() if a not in y)
    
    def lc_2469(self,Celsius):
    
        '''
        You are given a non-negative floating point number rounded to two decimal places celsius, 
        that denotes the temperature in Celsius.
        You should convert Celsius into Kelvin and Fahrenheit and return it as an array ans = [kelvin, fahrenheit].
        Return the array ans. Answers within 10-5 of the actual answer will be accepted.
        Note that:
        Kelvin = Celsius + 273.15
        Fahrenheit = Celsius * 1.80 + 32.00
 
        EXAMPLE:
        Input: celsius = 36.50
        Output: [309.65000,97.70000]
        Explanation: Temperature at 36.50 Celsius converted in Kelvin is 309.65 and converted in Fahrenheit is 97.70.
        '''

        Kelvin = Celsius + 273.15
        Fahrenheit = Celsius * 1.80 + 32.00
        return f'kelvin temp is {Kelvin} and Fahrenheit is {Fahrenheit}'
    
    
    def lc_2635(self,y):
    
        '''
        Given an integer array arr and a mapping function fn, return a new array with a transformation applied to each element.
        The returned array should be created such that returnedArray[i] = fn(arr[i], i).
        Please solve it without the built-in Array.map method.
        
        EXAMPLE:
        Input: arr = [1,2,3], fn = function plusone(n) { return n + 1; }
        Output: [2,3,4]
        Explanation:
        const newArray = map(arr, plusone); // [2,3,4]
        The function increases each value in the array by one.
        '''
        x = [i+1 for i in y]
        print(x)
        
    def lc_1480(self,nums,a=0):
    
        '''
        Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
        Return the running sum of nums
        
        EXAMPLE:
        Input: nums = [1,2,3,4]
        Output: [1,3,6,10]
        Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]
        '''

        res=[]
        for i in nums:
            a+=i
            res.append(a)
        return res
    
    def lc_1365(self,nmb):
    
        '''
        Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
        That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].
        Return the answer in an array.
        
        EXAMPLE:
        Input: nums = [8,1,2,2,3]
        Output: [4,0,1,1,3]
        Explanation: 
        For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
        For nums[1]=1 does not exist any smaller number than it.
        For nums[2]=2 there exist one smaller number than it (1). 
        For nums[3]=2 there exist one smaller number than it (1). 
        For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
        '''

        x = []
        for i in nmb:
            y = 0
            for j in nmb:
                if j<i:
                    y += 1
            x.append(y)
        return x

    def lc_2037(self, seats, students):

        '''
        There are n seats and n students in a room. You are given an array seats of length n,
        where seats[i] is the position of the ith seat. You are also given the array students
        of length n,where students[j] is the position of the jth student.

        You may perform the following move any number of times:

        Increase or decrease the position of the ith student by 1 (i.e., moving the ith student
        from position x to x + 1 or x - 1)
        Return the minimum number of moves required to move each student to a seat such that no
        two students are in the same seat.

        Note that there may be multiple seats or students in the same position at the beginning.

        Input: seats = [3,1,5], students = [2,7,4]
        Output: 4
        Explanation: The students are moved as follows:
        - The first student is moved from from position 2 to position 1 using 1 move.
        - The second student is moved from from position 7 to position 5 using 2 moves.
        - The third student is moved from from position 4 to position 3 using 1 move.
        In total, 1 + 2 + 1 = 4 moves were used
        '''

        seats.sort()
        students.sort()

        result = 0

        for i in range(len(seats)):
            result += abs(seats[i] - students[i])

        return result

    def lc_1290(self, head):

        '''

        Given head which is a reference node to a singly-linked list.
        The value of each node in the linked list is either 0 or 1.
        The linked list holds the binary representation of a number.

        Return the decimal value of the number in the linked list.

        The most significant bit is at the head of the linked list.


        Input: head = [1,0,1]
        Output: 5
        Explanation: (101) in base 2 = (5) in base 10
        '''

        x = ''.join([str(a) for a in head])
        y = int(x, 2)
        return y

    def lc_2455(self, x):

        '''
        Given an integer array nums of positive integers, return the average value
        of all even integers that are divisible by 3.

        Note that the average of n elements is the sum of the n elements divided by
        n and rounded down to the nearest integer.

        Input: nums = [1,3,6,10,12,15]
        Output: 9
        Explanation: 6 and 12 are even numbers that are divisible by 3. (6 + 12) / 2 = 9.
        '''

        y = [i for i in x if i % 2 == 0 and i % 3 == 0]

        z = sum(y) / len(y)
        print(z)

    def lc_2540(self, n1, n2):

        '''
        Given two integer arrays nums1 and nums2, sorted in non-decreasing order,
        return the minimum integer common to both arrays. If there is no common
        integer amongst nums1 and nums2, return -1.

        Note that an integer is said to be common to nums1 and nums2 if both arrays
        have at least one occurrence of that integer.


        Input: nums1 = [1,2,3], nums2 = [2,4]
        Output: 2
        Explanation: The smallest element common to both arrays is 2, so we return 2.
        '''

        for i in n1:
            if i in n2:
                return i
        return -1

    def lc_2000(self, x, y):

        '''
        Given a 0-indexed string word and a character ch, reverse the segment of word
        that starts at index 0 and ends at the index of the first occurrence of ch (inclus
        ive).If the character ch does not exist in word, do nothing.

        For example, if word = "abcdefd" and ch = "d", then you should reverse the segment
        that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
        Return the resulting string.

        Input: word = "abcdefd", ch = "d"
        Output: "dcbaefd"
        Explanation: The first occurrence of "d" is at index 3.
        Reverse the part of word from 0 to 3 (inclusive), the resulting string is "dcbaefd".
        '''

        if y in x:
            z = x.index(y)
            return x[:z + 1][::-1] + x[z + 1:]
        return x