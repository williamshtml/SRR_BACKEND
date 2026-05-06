import hashlib

def generate_transaction_hash(amount: float, sender: str, message: str) -> str:
    """
    Genera un hash SHA-256 único basado en los datos de la transacción
    para cumplir con la regla de No-Duplicados del SRR.
    """
    raw_str = f"{amount}{sender}{message}"
    return hashlib.sha256(raw_str.encode()).hexdigest()