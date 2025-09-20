class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        cipher = dict()
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        index = 0
        cipher[' '] = ' '
        for c in key:
            if c not in cipher:
                cipher[c] = alphabet[index]
                index += 1
    
        decoded = []
        for c in message:
            decoded.append(cipher[c])
        
        return ''.join(decoded)
                
