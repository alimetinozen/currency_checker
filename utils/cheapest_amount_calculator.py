from checker.models import Provider
from concurrent.futures import as_completed
from requests_futures.sessions import FuturesSession


def find_cheapest_amount(currency):
    provider_urls = list(Provider.objects.values_list('url', flat=True))

    selected_currency_amounts = []
    with FuturesSession() as session:
        futures = [session.get(pu) for pu in provider_urls]
        for future in as_completed(futures):
            resp = future.result()
            for r in resp.json():
                if r.get('code') == currency:
                    selected_currency_amounts.append(r.get('rate'))

    return {
        'currency': currency,
        'cheapest_amount': min(selected_currency_amounts)
    }
