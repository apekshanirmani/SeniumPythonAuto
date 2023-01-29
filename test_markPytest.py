import pytest as pytest


@pytest.mark.login
def test_login():
    print("Login function")


@pytest.mark.login
def test_forgot_password():
    print("Forgot Password")


@pytest.mark.login
def test_keep_me_login():
    print("Keep me login")


@pytest.mark.signUp
def test_sign_up():
    print("Sign Up")


@pytest.mark.signUp
def test_debit_validation():
    print("Debit")