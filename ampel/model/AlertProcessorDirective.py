#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : Ampel-alerts/ampel/model/AlertProcessingModel.py
# License           : BSD-3-Clause
# Author            : vb <vbrinnel@physik.hu-berlin.de>
# Date              : 14.10.2019
# Last Modified Date: 17.05.2020
# Last Modified By  : vb <vbrinnel@physik.hu-berlin.de>

from typing import Union, Optional, List, Dict, Literal
from ampel.type import ChannelId
from ampel.model.AmpelStrictModel import AmpelStrictModel
from ampel.model.T0AddModel import T0AddModel
from ampel.model.T1CombineModel import T1CombineModel
from ampel.model.T2ComputeModel import T2ComputeModel
from ampel.model.DataUnitModel import DataUnitModel
from ampel.model.AliasedDataUnitModel import AliasedDataUnitModel
from ampel.model.AutoStockMatchModel import AutoStockMatchModel

class AliasedFilterModel(AliasedDataUnitModel):
	reject: Optional[Dict[Literal['log', 'register'], Union[AliasedDataUnitModel, DataUnitModel]]]

class FilterModel(DataUnitModel):
	reject: Optional[Dict[Literal['log', 'register'], Union[AliasedDataUnitModel, DataUnitModel]]]

class AlertProcessingModel(AmpelStrictModel):
	channel: ChannelId
	dist_name: Optional[str]
	filter: Union[FilterModel, AliasedFilterModel]
	stock_match: Optional[AutoStockMatchModel]
	t0_add: T0AddModel
	t1_combine: Optional[List[T1CombineModel]]
	t2_compute: Optional[T2ComputeModel]
	stock_update: Union[DataUnitModel, AliasedDataUnitModel]