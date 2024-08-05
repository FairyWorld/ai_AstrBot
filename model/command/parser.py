import re

class CommandTokens():
    def __init__(self) -> None:
        self.tokens = []
        self.len = 0
        
    def get(self, idx: int):
        if idx >= self.len:
            return None
        return self.tokens[idx].strip()

class CommandParser():
    def __init__(self):
        pass
        
    def parse(self, message: str):
        cmd_tokens = CommandTokens()
        cmd_tokens.tokens = message.split(" ")
        cmd_tokens.len = len(cmd_tokens.tokens)
        return cmd_tokens
    
    def regex_match(self, message: str, command: str) -> bool:
        return re.search(command, message, re.MULTILINE) is not None
    