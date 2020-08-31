class Login_Page:

    loginXPath = {
            "tab_login": "//a[contains(text(), 'Sign in')]",
            "check_login_page": "//h3[contains(text(), 'Create an account')]",
            "create_email_box": "//input[contains(@id, 'email_create')]",
            "create_email_btn": "//button[contains(@id, 'SubmitCreate')]",
        }

    login_tab = loginXPath.get("tab_login")
    login_page_check = loginXPath.get("check_login_page")
    login_email_box = loginXPath.get("create_email_box")
    login_email_submit = loginXPath.get("create_email_btn")

