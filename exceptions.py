class WandBoxServiceError(Exception):
    """WandBoxのサービスから正常にレスポンスが返って来ない時の例外"""

    def __init__(self, status=None, body=None):
        super().__init__(status, body)
        self.status = status
        self.body = body

    def __str__(self):
        return "<%s> : <Status: %s>, <Body: %s>" % (self.__class__.__name__, self.status, self.body)
