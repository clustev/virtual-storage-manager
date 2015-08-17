
# Copyright 2014 Intel Corporation, All Rights Reserved.

# Licensed under the Apache License, Version 2.0 (the"License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#  http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.


from django.utils.translation import ugettext_lazy as _
from horizon import forms


import logging


LOG = logging.getLogger(__name__)


class CephUpgrade(forms.SelfHandlingForm):
    package_url = forms.CharField(label=_("Package URL"),
                            max_length=255,
                            min_length=1,
                            error_messages={
                            'required': _('This field is required.'),},
                            )

    key_url  = forms.CharField(label=_("Key URL"),
                            max_length=255,
                            min_length=1,
                            error_messages={
                            'required': _('This field is required.'),},
                            )


    def __init__(self, request, *args, **kwargs):
        super(CephUpgrade, self).__init__(request, *args, **kwargs)


    def handle(self, request, data):
        pass