# -*- coding: utf-8 -*-
# Copyright © 2008-2011 Kozea
# This file is part of Multicorn, licensed under a 3-clause BSD license.

from attest import Tests


all = Tests('.'.join((__name__, mod, 'suite'))
            for mod in ('test_queries',
                        'test_item'))
