#!/usr/bin/env python3
# @generated AUTOGENERATED file. Do not Change!

from dataclasses import dataclass
from datetime import datetime
from gql.gql.datetime_utils import DATETIME_FIELD
from gql.gql.graphql_client import GraphqlClient
from gql.gql.client import OperationException
from gql.gql.reporter import FailedOperationException
from functools import partial
from numbers import Number
from typing import Any, Callable, List, Mapping, Optional
from time import perf_counter
from dataclasses_json import DataClassJsonMixin

from .property_fragment import PropertyFragment, QUERY as PropertyFragmentQuery
from .add_link_input import AddLinkInput


QUERY: List[str] = PropertyFragmentQuery + ["""
mutation AddLinkMutation($input: AddLinkInput!) {
  addLink(input: $input) {
    id
    properties {
      ...PropertyFragment
    }
    services {
      id
    }
  }
}

"""]

@dataclass
class AddLinkMutation(DataClassJsonMixin):
    @dataclass
    class AddLinkMutationData(DataClassJsonMixin):
        @dataclass
        class Link(DataClassJsonMixin):
            @dataclass
            class Property(PropertyFragment):
                pass

            @dataclass
            class Service(DataClassJsonMixin):
                id: str

            id: str
            properties: List[Property]
            services: List[Service]

        addLink: Link

    data: AddLinkMutationData

    @classmethod
    # fmt: off
    def execute(cls, client: GraphqlClient, input: AddLinkInput) -> AddLinkMutationData.Link:
        # fmt: off
        variables = {"input": input}
        try:
            start_time = perf_counter()
            response_text = client.call(''.join(set(QUERY)), variables=variables)
            res = cls.from_json(response_text).data
            elapsed_time = perf_counter() - start_time
            client.reporter.log_successful_operation("AddLinkMutation", variables, elapsed_time)
            return res.addLink
        except OperationException as e:
            raise FailedOperationException(
                client.reporter,
                e.err_msg,
                e.err_id,
                "AddLinkMutation",
                variables,
            )
