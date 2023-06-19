"""Duck duck go Instant Answer API feature tests."""

from pytest_bdd import (
    given,
    scenarios,
    then,
    parsers,
)
import requests

EXTRA_TYPE = {
    'value': str,
}

DUCKDUCKGO_API= "http://api.duckduckgo.com"
scenarios(r'../../features/rest_api_tag.feature')  # , example_converters= dict(phrase= str)


#VVI-> Its imp to note that, both @given is imp. 2nd is imp for step defination as
# per feature and 1st one is needed as feature is scenario outline

@given(parsers.cfparse('The duckduck go API is queried with "{phrase:value}"',
                       extra_types=EXTRA_TYPE), target_fixture='get_response')
@given('The duckduck go API is queried with "<phrase>"', target_fixture='get_response')
def get_response(phrase):
    # format to search: http://api.duckduckgo.com/?q=x&format=json
    params= {"q":phrase, "format": "json"}
    response= requests.get(DUCKDUCKGO_API, params= params)
    return response

@then(parsers.cfparse('the response contains result for "{phrase:value}"', extra_types=EXTRA_TYPE))
@then('the response contains result for "<phrase>"')
def verify_response_contnet(get_response, phrase):
    print("My phrase is: ", phrase)
    #print("Content: ", get_response.json())
    api_phrase= get_response.json()["Heading"]
    #print("Phrase from API is: ", api_phrase)
    assert api_phrase.lower() == phrase.lower()


@then(parsers.cfparse('the response status code is "{code:value}"', extra_types= EXTRA_TYPE))
#@then('the response status code is "<code>"')
def verify_response_status(get_response, code):
    print("My code is: ", code)
    print("Status code: ", get_response.status_code)

