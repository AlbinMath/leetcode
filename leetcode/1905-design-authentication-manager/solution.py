class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.expiry = {}          # tokenId -> expiry time

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.expiry[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.expiry.get(tokenId, 0) > currentTime:
            self.expiry[tokenId] = currentTime + self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        return sum(1 for e in self.expiry.values() if e > currentTime)
