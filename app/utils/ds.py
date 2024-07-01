def update_immutable_querydict(immutable_dict, key, value):
    _mutable = immutable_dict._mutable
    immutable_dict._mutable = True
    immutable_dict[key] = value
    immutable_dict._mutable = _mutable
