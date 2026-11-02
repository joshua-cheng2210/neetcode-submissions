class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # initiation
        if len(s) != len(t):
            return False
        memory = {}

        # iteration
        print("iterating S")
        for character in s:
            if character not in memory:
                memory[character] = 0
            memory[character] += 1
        print(memory)
        print("iterating t")
        for character in t:
            if character not in memory:
                return False

            memory[character] -= 1

        print(memory)
        print("iterating memory")
        for character, num in memory.items():
            print(character, num)
            if num != 0:
                return False

        return True
