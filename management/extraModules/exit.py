class ZeroError(Exception):
    """Erro é gerado caso o usuário digite 0"""
    pass


class Exit:
    @staticmethod
    def end():
        raise ZeroError('Sair...')
