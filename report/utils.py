#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author:  ydbn2153
# Created: 2019-02-15
# Description: godlike recommend report module

def nameddict(name, props):
    class NamedDict(object):
        def __init__(self, *args, **kwargs):
            self.__store = {}.fromkeys(props)
            if args:
                for i, k in enumerate(props[:len(args)]):
                    self[k] = args[i]
            for k, v in kwargs.items():
                self[k] = v

        def __getattr__(self, key):
            # print '+', key
            if key.startswith('_NamedDict__'):
                return self.__dict__[key]
            else:
                return self.__store[key]

        def __setattr__(self, key, value):
            # print '-', key
            if key.startswith('_NamedDict__'):
                object.__setattr__(self, key, value)
            else:
                self.__setitem__(key, value)
                # self.__store[key] = value

        def __getitem__(self, key):
            return self.__store[key]

        def __setitem__(self, key, value):
            if key not in props:
                raise AttributeError("NamedDict(%s) has no attribute %s, avaliables are %s" % (
                    name, key, props))
            self.__store[key] = value

        def __dict__(self):
            return self.__store

        def __str__(self):
            return 'NamedDict(%s: %s)' % (name, str(self.__store))

    return NamedDict