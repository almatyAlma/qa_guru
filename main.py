browser.open('https://school.qa.guru')
browser.element('[name="email!!"]').type('qa_avtotester@tele2.kz').press_enter()
browser.element('[name="password"]').type('++++++').press_enter().press_enter()
browser.element('[class="page-header"]').should(have.text('Список тренингов'))