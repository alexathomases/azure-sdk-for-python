# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
# pylint: disable=wrong-import-position

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._patch import *  # pylint: disable=unused-wildcard-import


from ._models import (  # type: ignore
    CustomizationOptions,
    DeidentificationContent,
    DeidentificationJob,
    DeidentificationResult,
    DocumentDetails,
    DocumentLocation,
    JobCustomizationOptions,
    JobSummary,
    PhiEntity,
    PhiTaggerResult,
    SourceStorageLocation,
    StringIndex,
    TargetStorageLocation,
)

from ._enums import (  # type: ignore
    JobStatus,
    OperationState,
    OperationType,
    PhiCategory,
)
from ._patch import __all__ as _patch_all
from ._patch import *
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "CustomizationOptions",
    "DeidentificationContent",
    "DeidentificationJob",
    "DeidentificationResult",
    "DocumentDetails",
    "DocumentLocation",
    "JobCustomizationOptions",
    "JobSummary",
    "PhiEntity",
    "PhiTaggerResult",
    "SourceStorageLocation",
    "StringIndex",
    "TargetStorageLocation",
    "JobStatus",
    "OperationState",
    "OperationType",
    "PhiCategory",
]
__all__.extend([p for p in _patch_all if p not in __all__])  # pyright: ignore
_patch_sdk()
