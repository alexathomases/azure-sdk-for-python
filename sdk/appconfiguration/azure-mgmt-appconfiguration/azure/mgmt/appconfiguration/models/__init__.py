# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import ApiKey
from ._models_py3 import ApiKeyListResult
from ._models_py3 import CheckNameAvailabilityParameters
from ._models_py3 import ConfigurationStore
from ._models_py3 import ConfigurationStoreListResult
from ._models_py3 import ConfigurationStoreUpdateParameters
from ._models_py3 import DataPlaneProxyProperties
from ._models_py3 import DeletedConfigurationStore
from ._models_py3 import DeletedConfigurationStoreListResult
from ._models_py3 import EncryptionProperties
from ._models_py3 import ErrorAdditionalInfo
from ._models_py3 import ErrorDetail
from ._models_py3 import ErrorDetails
from ._models_py3 import ErrorResponse
from ._models_py3 import ErrorResponseAutoGenerated
from ._models_py3 import KeyValue
from ._models_py3 import KeyValueFilter
from ._models_py3 import KeyValueListResult
from ._models_py3 import KeyVaultProperties
from ._models_py3 import LogSpecification
from ._models_py3 import MetricDimension
from ._models_py3 import MetricSpecification
from ._models_py3 import NameAvailabilityStatus
from ._models_py3 import OperationDefinition
from ._models_py3 import OperationDefinitionDisplay
from ._models_py3 import OperationDefinitionListResult
from ._models_py3 import OperationProperties
from ._models_py3 import PrivateEndpoint
from ._models_py3 import PrivateEndpointConnection
from ._models_py3 import PrivateEndpointConnectionListResult
from ._models_py3 import PrivateEndpointConnectionReference
from ._models_py3 import PrivateLinkResource
from ._models_py3 import PrivateLinkResourceListResult
from ._models_py3 import PrivateLinkServiceConnectionState
from ._models_py3 import RegenerateKeyParameters
from ._models_py3 import Replica
from ._models_py3 import ReplicaListResult
from ._models_py3 import Resource
from ._models_py3 import ResourceIdentity
from ._models_py3 import ServiceSpecification
from ._models_py3 import Sku
from ._models_py3 import Snapshot
from ._models_py3 import SystemData
from ._models_py3 import TrackedResource
from ._models_py3 import UserIdentity

from ._app_configuration_management_client_enums import ActionsRequired
from ._app_configuration_management_client_enums import AuthenticationMode
from ._app_configuration_management_client_enums import CompositionType
from ._app_configuration_management_client_enums import ConfigurationResourceType
from ._app_configuration_management_client_enums import ConnectionStatus
from ._app_configuration_management_client_enums import CreateMode
from ._app_configuration_management_client_enums import CreatedByType
from ._app_configuration_management_client_enums import IdentityType
from ._app_configuration_management_client_enums import PrivateLinkDelegation
from ._app_configuration_management_client_enums import ProvisioningState
from ._app_configuration_management_client_enums import PublicNetworkAccess
from ._app_configuration_management_client_enums import ReplicaProvisioningState
from ._app_configuration_management_client_enums import SnapshotStatus
from ._patch import __all__ as _patch_all
from ._patch import *  # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "ApiKey",
    "ApiKeyListResult",
    "CheckNameAvailabilityParameters",
    "ConfigurationStore",
    "ConfigurationStoreListResult",
    "ConfigurationStoreUpdateParameters",
    "DataPlaneProxyProperties",
    "DeletedConfigurationStore",
    "DeletedConfigurationStoreListResult",
    "EncryptionProperties",
    "ErrorAdditionalInfo",
    "ErrorDetail",
    "ErrorDetails",
    "ErrorResponse",
    "ErrorResponseAutoGenerated",
    "KeyValue",
    "KeyValueFilter",
    "KeyValueListResult",
    "KeyVaultProperties",
    "LogSpecification",
    "MetricDimension",
    "MetricSpecification",
    "NameAvailabilityStatus",
    "OperationDefinition",
    "OperationDefinitionDisplay",
    "OperationDefinitionListResult",
    "OperationProperties",
    "PrivateEndpoint",
    "PrivateEndpointConnection",
    "PrivateEndpointConnectionListResult",
    "PrivateEndpointConnectionReference",
    "PrivateLinkResource",
    "PrivateLinkResourceListResult",
    "PrivateLinkServiceConnectionState",
    "RegenerateKeyParameters",
    "Replica",
    "ReplicaListResult",
    "Resource",
    "ResourceIdentity",
    "ServiceSpecification",
    "Sku",
    "Snapshot",
    "SystemData",
    "TrackedResource",
    "UserIdentity",
    "ActionsRequired",
    "AuthenticationMode",
    "CompositionType",
    "ConfigurationResourceType",
    "ConnectionStatus",
    "CreateMode",
    "CreatedByType",
    "IdentityType",
    "PrivateLinkDelegation",
    "ProvisioningState",
    "PublicNetworkAccess",
    "ReplicaProvisioningState",
    "SnapshotStatus",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
