def HasSymbol4Id(symbol_id):
    global id2symbol
    return symbol_id in id2symbol


def GetSymbol4Id(symbol_id):
    global id2symbol
    assert symbol_id in id2symbol
    return id2symbol[symbol_id]


def SetSymbol4Id(symbol_id, symbol):
    global id2symbol
    assert symbol_id not in id2symbol
    id2symbol[symbol_id] = symbol


id2symbol = {}


def HasSymbol4String(string):
    global string2symbol
    return string in string2symbol


def GetSymbol4String(string):
    global string2symbol
    return string2symbol[string]


def SetSymbol4String(string, symbol):
    assert not HasSymbol4String(string)
    global string2symbol
    string2symbol[string] = symbol


string2symbol = {}


def HasSymbol4SerializedOpConf(serialized_op_conf):
    global serialized_op_conf2symbol
    return serialized_op_conf in serialized_op_conf2symbol


def GetSymbol4SerializedOpConf(serialized_op_conf):
    global serialized_op_conf2symbol
    return serialized_op_conf2symbol[serialized_op_conf]


def SetSymbol4SerializedOpConf(serialized_op_conf, symbol):
    assert not HasSymbol4SerializedOpConf(serialized_op_conf)
    global serialized_op_conf2symbol
    serialized_op_conf2symbol[serialized_op_conf] = symbol


serialized_op_conf2symbol = {}


def HasSymbol4SerializedOpParallelAttribute(serialized_op_parallel_attribute):
    global serialized_op_parallel_attribute2symbol
    return serialized_op_parallel_attribute in serialized_op_parallel_attribute2symbol


def GetSymbol4SerializedOpParallelAttribute(serialized_op_parallel_attribute):
    global serialized_op_parallel_attribute2symbol
    return serialized_op_parallel_attribute2symbol[serialized_op_parallel_attribute]


def SetSymbol4SerializedOpParallelAttribute(serialized_op_parallel_attribute, symbol):
    assert not HasSymbol4SerializedOpParallelAttribute(serialized_op_parallel_attribute)
    global serialized_op_parallel_attribute2symbol
    serialized_op_parallel_attribute2symbol[serialized_op_parallel_attribute] = symbol


serialized_op_parallel_attribute2symbol = {}


def HasSymbol4JobConf(job_conf):
    global job_conf_id2symbol
    return id(job_conf) in job_conf_id2symbol


def GetSymbol4JobConf(job_conf):
    global job_conf_id2symbol
    return job_conf_id2symbol[id(job_conf)]


def SetSymbol4JobConf(job_conf, symbol):
    assert not HasSymbol4JobConf(job_conf)
    global job_conf_id2symbol
    job_conf_id2symbol[id(job_conf)] = symbol


job_conf_id2symbol = {}


def HasSymbol4SerializedParallelConf(serialized_parallel_conf):
    global serialized_parallel_conf2symbol
    return serialized_parallel_conf in serialized_parallel_conf2symbol


def GetSymbol4SerializedParallelConf(serialized_parallel_conf):
    global serialized_parallel_conf2symbol
    return serialized_parallel_conf2symbol[serialized_parallel_conf]


def SetSymbol4SerializedParallelConf(serialized_parallel_conf, symbol):
    assert not HasSymbol4SerializedParallelConf(serialized_parallel_conf)
    global serialized_parallel_conf2symbol
    serialized_parallel_conf2symbol[serialized_parallel_conf] = symbol


serialized_parallel_conf2symbol = {}


def HasSymbol4SerializedScopeProto(serialized_scope_proto):
    global serialized_scope_proto2symbol
    return serialized_scope_proto in serialized_scope_proto2symbol


def GetSymbol4SerializedScopeProto(serialized_scope_proto):
    global serialized_scope_proto2symbol
    return serialized_scope_proto2symbol[serialized_scope_proto]


def SetSymbol4SerializedScopeProto(serialized_scope_proto, symbol):
    assert not HasSymbol4SerializedScopeProto(serialized_scope_proto)
    global serialized_scope_proto2symbol
    serialized_scope_proto2symbol[serialized_scope_proto] = symbol


serialized_scope_proto2symbol = {}
