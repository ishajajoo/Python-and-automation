import pytest
from src.swag_labs.step.login_step import Login_step


#@pytest.mark.usefixtures("set_up")
class Test_login:

    @pytest.mark.smoke
    def test_login(set_up):
        # l = Login_step()
        print("hello")
        # l.login("standard_user", "secret_sauce")
