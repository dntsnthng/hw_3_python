from selene import browser, be, have



def test_open_google():
    browser.open("https://www.google.com")
    browser.element('[name="q"]').should(be.blank).type('jfdhgkjdfhgjkfdhgfdkg').press_enter()
    browser.element('[id="search"]').should(have.text('Как стать супергероям за 24 часа без смс и регистрации'))


