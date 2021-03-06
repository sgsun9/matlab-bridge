function [descriptor] = pb_descriptor_FrameLocationList()
%pb_descriptor_FrameLocationList Returns the descriptor for message FrameLocationList.
%   function [descriptor] = pb_descriptor_FrameLocationList()
%
%   See also pb_read_FrameLocationList

  descriptor = struct( ...
    'name', 'FrameLocationList', ...
    'full_name', 'FrameLocationList', ...
    'filename', 'protobuf_defs.proto', ...
    'containing_type', '', ...
    'fields', [ ...
      struct( ...
        'name', 'framelocation', ...
        'full_name', 'FrameLocationList.framelocation', ...
        'index', 1, ...
        'number', uint32(1), ...
        'type', uint32(11), ...
        'matlab_type', uint32(9), ...
        'wire_type', uint32(2), ...
        'label', uint32(3), ...
        'default_value', struct([]), ...
        'read_function', @(x) pb_read_FrameLocation(x{1}, x{2}, x{3}), ...
        'write_function', @pblib_generic_serialize_to_string, ...
        'options', struct('packed', false) ...
      ) ...
    ], ...
    'extensions', [ ... % Not Implemented
    ], ...
    'nested_types', [ ... % Not implemented
    ], ...
    'enum_types', [ ... % Not Implemented
    ], ...
    'options', [ ... % Not Implemented
    ] ...
  );

  descriptor.field_indeces_by_number = java.util.HashMap;
  put(descriptor.field_indeces_by_number, uint32(1), 1);

