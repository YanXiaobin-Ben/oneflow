#include "oneflow/core/eager/eager_util.h"
#include "oneflow/core/eager/eager_symbol.pb.h"
#include "oneflow/core/vm/vm_util.h"
#include "oneflow/core/vm/instruction.pb.h"
#include "oneflow/core/eager/eager_symbol_storage.h"
#include "oneflow/core/job/job_desc.h"
#include "oneflow/core/job/scope.h"
#include "oneflow/core/job/placement.pb.h"
#include "oneflow/core/operator/op_conf.pb.h"
#include "oneflow/core/operator/op_attribute.pb.h"
#include "oneflow/core/common/protobuf.h"
#include "oneflow/core/common/util.h"

namespace oneflow {
namespace eager {

namespace {

void StorageAdd(const EagerSymbol& symbol) {
  int64_t symbol_id = symbol.symbol_id();
  if (symbol.has_string_symbol()) {
    Global<vm::SymbolStorage<std::string>>::Get()->Add(symbol_id, symbol.string_symbol());
  } else if (symbol.has_scope_symbol()) {
    Global<vm::SymbolStorage<Scope>>::Get()->Add(symbol_id, symbol.scope_symbol());
  } else if (symbol.has_job_conf_symbol()) {
    Global<vm::SymbolStorage<JobDesc>>::Get()->Add(symbol_id, symbol.job_conf_symbol());
  } else if (symbol.has_parallel_conf_symbol()) {
    Global<vm::SymbolStorage<ParallelDesc>>::Get()->Add(symbol_id, symbol.parallel_conf_symbol());
  } else if (symbol.has_op_conf_symbol()) {
    Global<vm::SymbolStorage<OperatorConf>>::Get()->Add(symbol_id, symbol.op_conf_symbol());
  } else if (symbol.has_op_parallel_attribute_symbol()) {
    Global<vm::SymbolStorage<OpParallelAttribute>>::Get()->Add(
        symbol_id, symbol.op_parallel_attribute_symbol());
  } else {
    UNIMPLEMENTED();
  }
}

Maybe<void> RunLogicalInstruction(const vm::InstructionListProto& instruction_list_proto,
                                  const EagerSymbolList& eager_symbol_list) {
  for (const auto& eager_symbol : eager_symbol_list.eager_symbol()) { StorageAdd(eager_symbol); }
  return vm::Run(instruction_list_proto);
}

Maybe<void> RunPhysicalInstruction(const vm::InstructionListProto& instruction_list_proto,
                                   const EagerSymbolList& eager_symbol_list) {
  for (const auto& eager_symbol : eager_symbol_list.eager_symbol()) { StorageAdd(eager_symbol); }
  return vm::Run(instruction_list_proto);
}

}  // namespace

Maybe<void> RunPhysicalInstruction(const std::string& instruction_list_proto_str,
                                   const std::string& eager_symbol_list_str) {
  vm::InstructionListProto instruction_list_proto;
  CHECK_OR_RETURN(TxtString2PbMessage(instruction_list_proto_str, &instruction_list_proto))
      << "InstructionListProto parse failed";
  EagerSymbolList eager_symbol_list;
  CHECK_OR_RETURN(TxtString2PbMessage(eager_symbol_list_str, &eager_symbol_list))
      << "EagerSymbolList parse failed";
  return RunPhysicalInstruction(instruction_list_proto, eager_symbol_list);
}

Maybe<void> RunLogicalInstruction(const std::string& instruction_list_proto_str,
                                  const std::string& eager_symbol_list_str) {
  vm::InstructionListProto instruction_list_proto;
  CHECK_OR_RETURN(TxtString2PbMessage(instruction_list_proto_str, &instruction_list_proto))
      << "InstructionListProto parse failed";
  EagerSymbolList eager_symbol_list;
  CHECK_OR_RETURN(TxtString2PbMessage(eager_symbol_list_str, &eager_symbol_list))
      << "EagerSymbolList parse failed";
  return RunLogicalInstruction(instruction_list_proto, eager_symbol_list);
}

}  // namespace eager
}  // namespace oneflow
