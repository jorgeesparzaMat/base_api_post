class SalidaControlada(Exception):
    def __init__(
        self, codigo_error: str, user_message: str, technical_message: str
    ) -> None:
        self.codigo_error = codigo_error
        self.user_message = user_message
        self.technical_message = technical_message
