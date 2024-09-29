@given(u'I open the app')
def step_impl(context):
    print(u'STEP: Given I open the app')


@when(u'I enter the username and password')
def step_impl(context):
    print(u'STEP: When I enter the username and password')


@when(u'I tap the login button')
def step_impl(context):
    print(u'STEP: When I tap the login button')


@then(u'I should be logged into the app')
def step_impl(context):
    print(u'STEP: Then I should be logged into the app')