import random
def generate_otp(length=4):
    if length<=0:
        raise valueError("OTP length must be positive.")
    otp=''.join([str(random.randint(0,9)) for _ in range(length)])
    return otp

otp=generate_otp()
print("Your OTP is:",otp)