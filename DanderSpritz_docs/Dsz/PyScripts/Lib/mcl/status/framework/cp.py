# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: cp.py
LLA_SUCCESS = 0
LLA_ERROR_OUT_OF_MEMORY = 4026531841L
LLA_ERROR_INVALID_PARAM = 4026531842L
LLA_ERROR_NOT_SUPPORTED = 4026531843L
LLA_ERROR_NO_PERMISSION = 4026531844L
LLA_ERROR_TIMEOUT = 4026531845L
LLA_ERROR_NOT_FOUND = 4026531846L
LLA_ERROR_NOT_INITIALIZED = 4026531847L
LLA_ERROR_BUSY = 4026531848L
LLA_ERROR_BAD_ADDRESS = 4026531849L
LLA_ERROR_LIMIT_EXCEEDED = 4026531850L
LLA_ERROR_INVALID_STACKSIZE = 4026531851L
LLA_ERROR_INVALID_PRIORITY = 4026531852L
LLA_ERROR_INVALID_ATTRIBUTE = 4026531853L
LLA_ERROR_WILL_DEADLOCK = 4026531854L
LLA_ERROR_TIME_TOO_LARGE = 4026531855L
LLA_ERROR_THREAD_FAILURE = 4026531856L
CHM_ERROR_RPC_TIMEOUT = 3758096385L
CHM_ERROR_PROVIDER_NOT_FOUND = 3758096386L
CHM_ERROR_INVALID_PROCEDURE = 3758096387L
CHM_ERROR_CANCELED = 3758096388L
CHM_ERROR_MARSHALING_FAILED = 3758096389L
CHM_ERROR_DEMARSHALING_FAILED = 3758096390L
CHM_ERROR_OUT_OF_MEMORY = 3758096391L
CHM_ERROR_API_NOT_FOUND = 3758096392L
CHM_ERROR_MODULE_IN_USE = 3758096393L
CHM_ERROR_MODULE_NOT_FOUND = 3758096394L
CHM_ERROR_REGISTER_API_FAILED = 3758096395L
CHM_ERROR_API_IN_USE = 3758096396L
CHM_ERROR_MODULE_STOPPING = 3758096397L
CHM_ERROR_CREATING_MODULE = 3758096398L
CHM_ERROR_MODULE_LOAD_FAILURE = 3758096399L
CHM_ERROR_LOADER_NOT_FOUND = 3758096400L
CHM_ERROR_MODULE_UNLOAD_FAILURE = 3758096401L
CHM_ERROR_TOO_MANY_MODULES = 3758096402L
CHM_ERROR_REINITIALIZATION = 3758096403L
CHM_ERROR_API_COULD_NOT_ATTACH = 3758096404L
CHM_ERROR_API_COULD_NOT_DETACH = 3758096405L
CHM_ERROR_API_NOT_ACQUIRED = 3758096406L
CHM_ERROR_API_NOT_REGISTERED = 3758096407L
CHM_ERROR_TIMEOUT = 3758096408L
CHM_COMMS_ERROR_TIMEOUT = 3758096640L
CHM_COMMS_ERROR_SEND_NOT_PERMITTED = 3758096641L
CHM_COMMS_ERROR_RECV_NOT_PERMITTED = 3758096642L
CHM_COMMS_ERROR_NO_ROUTE = 3758096643L
CHM_COMMS_ERROR_PRIORITY_TOO_LOW = 3758096644L
CHM_COMMS_ERROR_NO_LOCAL_HOST_ADDRESS = 3758096645L
CHM_COMMS_ERROR_INTERNAL_ERROR = 3758096646L
CHM_COMMS_ERROR_BAD_PACKET = 3758096647L
CHM_COMMS_ERROR_RPC_ACCESS_DENIED = 3758096648L
CHM_COMMS_ERROR_RPC_NOT_FOUND = 3758096649L
CHM_COMMS_ERROR_RPC_NOT_CANCELED = 3758096650L
CHM_COMMS_ERROR_SECURITY_FAILURE = 3758096651L
CHM_COMMS_ERROR_COULD_NOT_FRAGMENT = 3758096652L
CHM_COMMS_ERROR_ROUTE_DOWN = 3758096653L
CHM_COMMS_ERROR_RPC_COMPLETED = 3758096654L
errorStrings = {LLA_ERROR_OUT_OF_MEMORY: 'LLA: Memory allocation failed',
   LLA_ERROR_INVALID_PARAM: 'LLA: Invalid parameter(s)',
   LLA_ERROR_NOT_SUPPORTED: 'LLA: Not supported',
   LLA_ERROR_NO_PERMISSION: 'LLA: Permission check failed',
   LLA_ERROR_TIMEOUT: 'LLA: Operation timed out',
   LLA_ERROR_NOT_FOUND: 'LLA: Object not found',
   LLA_ERROR_NOT_INITIALIZED: 'LLA: Object not initialized',
   LLA_ERROR_BUSY: 'LLA: Object is busy',
   LLA_ERROR_BAD_ADDRESS: 'LLA: Invalid pointer',
   LLA_ERROR_LIMIT_EXCEEDED: 'LLA: Limit exceeded',
   LLA_ERROR_INVALID_STACKSIZE: 'LLA: Invalid stack size',
   LLA_ERROR_INVALID_PRIORITY: 'LLA: Invalid priority',
   LLA_ERROR_INVALID_ATTRIBUTE: 'LLA: Invalid attribute',
   LLA_ERROR_WILL_DEADLOCK: 'LLA: Will deadlock',
   LLA_ERROR_TIME_TOO_LARGE: 'LLA: Time too large',
   LLA_ERROR_THREAD_FAILURE: 'LLA: Unspecified thread failure',
   CHM_ERROR_RPC_TIMEOUT: 'CHM: A remote call timed out',
   CHM_ERROR_PROVIDER_NOT_FOUND: 'CHM: The specified provider could not be located',
   CHM_ERROR_INVALID_PROCEDURE: 'CHM: The procedure specified was invalid for the provider',
   CHM_ERROR_CANCELED: 'CHM: A call was cancelled',
   CHM_ERROR_MARSHALING_FAILED: 'CHM: Failed to marshal call data',
   CHM_ERROR_DEMARSHALING_FAILED: 'CHM: Failed to demarshal call data',
   CHM_ERROR_OUT_OF_MEMORY: 'CHM: Out of memory',
   CHM_ERROR_API_NOT_FOUND: 'CHM: API not found',
   CHM_ERROR_MODULE_IN_USE: 'CHM: Module is in use',
   CHM_ERROR_MODULE_NOT_FOUND: 'CHM: Module was not found',
   CHM_ERROR_REGISTER_API_FAILED: 'CHM: API registration failed',
   CHM_ERROR_API_IN_USE: 'CHM: API is in use',
   CHM_ERROR_MODULE_STOPPING: 'CHM: Module is stopping',
   CHM_ERROR_CREATING_MODULE: 'CHM: Module creation error',
   CHM_ERROR_MODULE_LOAD_FAILURE: 'CHM: Module load failure',
   CHM_ERROR_LOADER_NOT_FOUND: "CHM: Loader wasn't found",
   CHM_ERROR_MODULE_UNLOAD_FAILURE: 'CHM: Module failed to unload',
   CHM_ERROR_TOO_MANY_MODULES: 'CHM: Maximum number of modules was exceeded',
   CHM_ERROR_REINITIALIZATION: 'CHM: Initialization has been performed twice',
   CHM_ERROR_API_COULD_NOT_ATTACH: 'CHM: API could not be attached',
   CHM_ERROR_API_COULD_NOT_DETACH: 'CHM: API could not be detached',
   CHM_ERROR_API_NOT_ACQUIRED: 'CHM: API was not acquired, but attempted release',
   CHM_ERROR_API_NOT_REGISTERED: 'CHM: API was not registered, but attempted unregister',
   CHM_ERROR_TIMEOUT: 'CHM: The framework timed out',
   CHM_COMMS_ERROR_TIMEOUT: 'COMMS: Timed out while sending a message',
   CHM_COMMS_ERROR_SEND_NOT_PERMITTED: 'COMMS: Send to destination address is not permitted',
   CHM_COMMS_ERROR_RECV_NOT_PERMITTED: 'COMMS: Receive from address is not permitted',
   CHM_COMMS_ERROR_NO_ROUTE: 'COMMS: There is no route to the destination address',
   CHM_COMMS_ERROR_PRIORITY_TOO_LOW: 'COMMS: Message was discarded due to low message priority',
   CHM_COMMS_ERROR_NO_LOCAL_HOST_ADDRESS: 'COMMS: Comms has not been configured with a network address',
   CHM_COMMS_ERROR_INTERNAL_ERROR: 'COMMS: Comms internal state is corrupted',
   CHM_COMMS_ERROR_BAD_PACKET: 'COMMS: A packet received from a Link is corrupted',
   CHM_COMMS_ERROR_RPC_ACCESS_DENIED: 'COMMS: Access was denied on the remote end for the requested RPC',
   CHM_COMMS_ERROR_RPC_NOT_FOUND: 'COMMS: RPC was not found in list of outstanding calls',
   CHM_COMMS_ERROR_RPC_NOT_CANCELED: 'COMMS: RPC was found, but could not be canceled',
   CHM_COMMS_ERROR_SECURITY_FAILURE: 'COMMS: The RPC was dropped due to a security-related failure',
   CHM_COMMS_ERROR_COULD_NOT_FRAGMENT: 'COMMS: The message could not be fragmented',
   CHM_COMMS_ERROR_ROUTE_DOWN: 'COMMS: Route to the destination address is temporarily unavailable',
   CHM_COMMS_ERROR_RPC_COMPLETED: 'COMMS: RPC was found, but has already completed'
   }