
# solution (accepted)
def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
	wordList = set(wordList)
	queue = collections.deque([[beginWord, 1]])
	charList = set()
	
	for word in wordList:
		for char in word:
			charList.add(char)

	while queue:
		word, length = queue.popleft()
		
		if word == endWord:
			return length
		
		for i in range(len(word)):
			for c in charList:
				new_word = word[:i] + c + word[i+1:]
				if new_word in wordList:
					wordList.discard(new_word)
					queue.append([new_word, length+1])
	
	return 0
