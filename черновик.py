message = "s"

if not message:
    print('asd')
else:
    print('sadasd')
    
@pytest.mark.parametrize("email", config.settings.PAYLOAD["EMAIL_NEGATIVE"], ids=str)
def test_negative_email_add_user(email):
    send_and_assert("email", email, 400, message_uncorrect["email"] )