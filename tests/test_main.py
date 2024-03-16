from selene import browser, be, have



def test_open_google():
    browser.open("https://www.google.com")
    browser.element('[name="q"]').should(be.blank).type('Россия').press_enter()
    browser.element('[id="search"]').should(have.text('Ро1ссия'))

