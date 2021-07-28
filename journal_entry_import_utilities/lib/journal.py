from typing import List, Optional

from cachetools import TTLCache, cached
from odoo import exceptions

MAP_CACHE = TTLCache(maxsize=1, ttl=10)


@cached(MAP_CACHE)
def get_account_to_journal_mapping(env, model: str):
    return {
        mapping.account_id.id if mapping.account_id else None: mapping
        for mapping in env[model].search([])
    }


def get_journal(env, account_ids: List[Optional[str]], model: str):
    """Get the correct journal for the account ids from the given model..

    :param model: model of mapping
    :param env: odoo environment to use
    :param account_ids: list of accounts
    :param exceptions.UserError: if no journal is found
    """

    # Gets full mapping once
    account_to_journal_mapping = get_account_to_journal_mapping(env, model)
    default = account_to_journal_mapping.get(None)

    mappings = list(
        {account_to_journal_mapping.get(account_id) for account_id in account_ids}
    )

    # Remove null values (if mapping does not exist for given account id)
    mappings = [m for m in mappings if m]

    # Take the map with the highest sequence
    mappings.sort(key=lambda m: m.sequence)
    if mappings:
        return mappings[0].journal_id
    elif default:
        return default.journal_id

    raise exceptions.UserError(
        f"Could not find journal mapped to accounts: {account_ids}."
    )
