class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # initiation:
        # ascii_rep = [0] * 26
        memory = {}

        # iterations
        for word in strs:
            ascii_rep = [0] * 26
            for x in word:
                character_ord = ord(x) - ord('a')
                ascii_rep[character_ord] += 1
            
            # compare and group
            if tuple(ascii_rep) not in memory:
                memory[tuple(ascii_rep)] = [word]
            else:
                memory[tuple(ascii_rep)].append(word)

        # output
        # get the group of lists in the memory dictionary
        output = []
        for key, value in memory.items():
            output.append(value)

        return output

        