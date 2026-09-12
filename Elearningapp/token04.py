import base64
import json
import os
import time
import random
import struct
from hashlib import sha256
from Crypto.Cipher import AES


def generate_token04(
    app_id,
    user_id,
    secret,
    effective_time_in_seconds,
    payload=""
):
    """
    Generate ZEGOCLOUD Token04.

    app_id: ZEGOCLOUD App ID
    user_id: unique user ID
    secret: ZEGOCLOUD Server Secret
    effective_time_in_seconds: token validity
    payload: optional JSON payload
    """

    # Check App ID
    if not isinstance(app_id, int) or app_id <= 0:
        raise ValueError("Invalid App ID")

    # Check User ID
    if not user_id:
        raise ValueError("User ID cannot be empty")

    # Check Server Secret
    if not secret:
        raise ValueError("Server Secret cannot be empty")

    secret = secret.encode("utf-8")

    if len(secret) not in [16, 24, 32]:
        raise ValueError(
            "Server Secret must be 16, 24, or 32 bytes"
        )

    # Current time
    create_time = int(time.time())

    # Expiration time
    expire_time = create_time + effective_time_in_seconds

    # Random nonce
    nonce = random.randint(
        -2147483648,
        2147483647
    )

    # Token information
    token_info = {
        "app_id": app_id,
        "user_id": user_id,
        "nonce": nonce,
        "ctime": create_time,
        "expire": expire_time,
        "payload": payload
    }

    # Convert to JSON
    token_info_json = json.dumps(
        token_info,
        separators=(",", ":")
    ).encode("utf-8")

    # Generate checksum
    checksum = sha256(token_info_json).digest()

    # AES encryption
    iv = os.urandom(16)

    cipher = AES.new(
        secret,
        AES.MODE_CBC,
        iv
    )

    # PKCS7 padding
    padding_length = 16 - (len(token_info_json) % 16)

    padded_data = (
        token_info_json +
        bytes([padding_length]) * padding_length
    )

    encrypted_data = cipher.encrypt(padded_data)

    # Build token data
    token_data = (
        struct.pack(">Q", expire_time)
        + struct.pack(">H", len(iv))
        + iv
        + struct.pack(">H", len(encrypted_data))
        + encrypted_data
        + checksum
    )

    # Base64 encode
    token_base64 = base64.b64encode(
        token_data
    ).decode("utf-8")

    # Add Token04 version
    token = "04" + token_base64

    return token