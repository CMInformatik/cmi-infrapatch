import logging as log
import re
from dataclasses import dataclass
from typing import Any, Optional, Sequence, Union

from infrapatch.core.models.versioned_resource import VersionedResource


@dataclass
class VersionedTerraformResource(VersionedResource):
    _base_domain: Union[str, None] = None
    _identifier: Union[str, None] = None
    _source: Union[str, None] = None

    @property
    def source(self) -> Union[str, None]:
        return self._source

    @property
    def base_domain(self) -> Optional[str]:
        return self._base_domain

    @property
    def resource_name(self):
        raise NotImplementedError()

    @property
    def identifier(self) -> Union[str, None]:
        return self._identifier


@dataclass
class TerraformModule(VersionedTerraformResource):
    def __post_init__(self):
        if self._source is None:
            raise Exception("Source is None.")
        self.source = self._source

    @property
    def source(self) -> Union[str, None]:
        return self._source

    @property
    def resource_name(self):
        return "Module"

    @source.setter
    def source(self, source: str):
        source_lower_case = source.lower()
        self._source = source_lower_case
        self._newest_version = None
        if re.match(r"^[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+/[a-zA-Z0-9-_]+/[a-zA-Z0-9-_]+/[a-zA-Z0-9-_]+$", source_lower_case):
            log.debug(f"Source '{source_lower_case}' is from a generic registry.")
            self._base_domain = source_lower_case.split("/")[0]
            self._identifier = "/".join(source_lower_case.split("/")[1:])
        elif re.match(r"^[a-zA-Z0-9-_]+/[a-zA-Z0-9-_]+/[a-zA-Z0-9-_]+$", source_lower_case):
            log.debug(f"Source '{source_lower_case}' is from the public registry.")
            self._identifier = source_lower_case
        else:
            raise Exception(f"Source '{source_lower_case}' is not a valid terraform resource source.")


@dataclass
class TerraformProvider(VersionedTerraformResource):
    def __post_init__(self):
        if self._source is None:
            raise Exception("Source is None.")
        self.source = self._source

    @property
    def source(self) -> Union[str, None]:
        return self._source

    @property
    def resource_name(self):
        return "Module"

    @source.setter
    def source(self, source: str) -> None:
        source_lower_case = source.lower()
        self._source = source_lower_case
        self._newest_version = None
        if re.match(r"^[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+/[a-zA-Z0-9-_]+/[a-zA-Z0-9-_]+$", source_lower_case):
            log.debug(f"Source '{source_lower_case}' is from a generic registry.")
            self._base_domain = source_lower_case.split("/")[0]
            self._identifier = "/".join(source_lower_case.split("/")[1:])
        elif re.match(r"^[a-zA-Z0-9-_]+/[a-zA-Z0-9-_]+$", source_lower_case):
            log.debug(f"Source '{source_lower_case}' is from the public registry.")
            self._identifier = source_lower_case
        else:
            raise Exception(f"Source '{source_lower_case}' is not a valid terraform resource source.")


def get_upgradable_resources(resources: Sequence[VersionedTerraformResource]) -> Sequence[VersionedTerraformResource]:
    return [resource for resource in resources if not resource.check_if_up_to_date()]


def from_terraform_resources_to_dict_list(terraform_resources: Sequence[VersionedTerraformResource]) -> Sequence[dict]:
    return [terraform_resource.to_dict() for terraform_resource in terraform_resources]
