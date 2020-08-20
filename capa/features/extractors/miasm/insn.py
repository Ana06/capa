import capa.features.extractors.helpers
from capa.features import String, Characteristic
from capa.features.insn import API, Number, Offset, Mnemonic


def interface_extract_instruction_XXX(f, bb, insn):
    """
    parse features from the given instruction.
    args:
      f (viv_utils.Function): the function to process.
      bb (viv_utils.BasicBlock): the basic block to process.
      insn (vivisect...Instruction): the instruction to process.
    yields:
      (Feature, int): the feature and the address at which its found.
    """
    yield NotImplementedError("feature"), NotImplementedError("virtual address")


def get_imports(vw):
    """
    caching accessor to vivisect workspace imports.
    this is necessary due to the performance issue identified here:
        https://ghe.eng.fireeye.com/FLARE/capa/issues/137#issuecomment-156518
    """
    raise NotImplementedError()


def extract_insn_api_features(f, bb, insn):
    """parse API features from the given instruction."""
    raise NotImplementedError()


def extract_insn_number_features(f, bb, insn):
    """parse number features from the given instruction."""
    raise NotImplementedError()


def read_string(vw, offset):
    raise NotImplementedError()


def extract_insn_string_features(f, bb, insn):
    """parse string features from the given instruction."""
    raise NotImplementedError()


def extract_insn_offset_features(f, bb, insn):
    """parse structure offset features from the given instruction."""
    raise NotImplementedError()


def is_security_cookie(f, bb, insn):
    """
    check if an instruction is related to security cookie checks
    """
    raise NotImplementedError()


def extract_insn_nzxor_characteristic_features(f, bb, insn):
    """
    parse non-zeroing XOR instruction from the given instruction.
    ignore expected non-zeroing XORs, e.g. security cookies.
    """
    raise NotImplementedError()


def extract_insn_mnemonic_features(f, bb, insn):
    """parse mnemonic features from the given instruction."""
    raise NotImplementedError()


def extract_insn_peb_access_characteristic_features(f, bb, insn):
    """
    parse peb access from the given function. fs:[0x30] on x86, gs:[0x60] on x64
    """
    raise NotImplementedError()


def extract_insn_segment_access_features(f, bb, insn):
    """ parse the instruction for access to fs or gs """
    raise NotImplementedError()


def get_section(vw, va):
    raise NotImplementedError()


def extract_insn_cross_section_cflow(f, bb, insn):
    """
    inspect the instruction for a CALL or JMP that crosses section boundaries.
    """
    raise NotImplementedError()


# this is a feature that's most relevant at the function scope,
# however, its most efficient to extract at the instruction scope.
def extract_function_calls_from(f, bb, insn):
    raise NotImplementedError()


def extract_features(f, bb, insn):
    """
    extract features from the given insn.
    args:
      f (viv_utils.Function): the function from which to extract features
      bb (viv_utils.BasicBlock): the basic block to process.
      insn (vivisect...Instruction): the instruction to process.
    yields:
      Feature, set[VA]: the features and their location found in this insn.
    """
    for insn_handler in INSTRUCTION_HANDLERS:
        for feature, va in insn_handler(f, bb, insn):
            yield feature, va


INSTRUCTION_HANDLERS = (
    extract_insn_api_features,
    extract_insn_number_features,
    extract_insn_string_features,
    extract_insn_offset_features,
    extract_insn_nzxor_characteristic_features,
    extract_insn_mnemonic_features,
    extract_insn_peb_access_characteristic_features,
    extract_insn_cross_section_cflow,
    extract_insn_segment_access_features,
    extract_function_calls_from,
)
