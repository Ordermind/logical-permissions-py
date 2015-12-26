from logical_permissions.interfaces.LogicalPermissionsBase import LogicalPermissionsBase
from logical_permissions.exceptions import *

class LogicalPermissions(LogicalPermissionsBase):
  
  def __init__(self):
    self.__types = {}
    self.__bypass_callback = None

  def addType(self, name, callback):
    if(type(name) is not str):
      raise InvalidArgumentTypeException('The name parameter must be a string.')
    if not name:
      raise InvalidArgumentValueException('The name parameter cannot be empty.')
    if not hasattr(callback, '__call__'):
      raise InvalidArgumentTypeException('The callback parameter must be a callable data type.')

    types = self.getTypes()
    types[name] = callback
    self.setTypes(types)
  
  def removeType(self, name):
    if(type(name) is not str):
      raise InvalidArgumentTypeException('The name parameter must be a string.')
    if not name:
      raise InvalidArgumentValueException('The name parameter cannot be empty.')
    if not self.typeExists(name):
      raise PermissionTypeNotRegisteredException('The permission type "{0}" has not been registered. Please use LogicalPermissions::addType() or LogicalPermissions::setTypes() to register permission types.'.format(name))
    
    types = self.getTypes()
    types.pop(name, None)
    self.setTypes(types)
    
  def typeExists(self, name):
    if(type(name) is not str):
      raise InvalidArgumentTypeException('The name parameter must be a string.')
    if not name:
      raise InvalidArgumentValueException('The name parameter cannot be empty.')

    types = self.getTypes()
    return name in types

  def getTypeCallback(self, name):
    pass

  def getTypes(self):
    return self.__types

  def setTypes(self, types):
    self.__types = types
  
  def getBypassCallback(self):
    pass 
    
  def setBypassCallback(self, callback):
    pass 

  def checkAccess(self, permissions, context):
    pass
  
  def __checkBypassAccess(self, context):
    pass
  
  def __dispatch(self, permissions, context, type = None):
    pass
  
  def __processAND(self, permissions, context, type = None):
    pass
  
  def __processNAND(self, permissions, context, type = None):
    pass
  
  def __processOR(self, permissions, context, type = None):
    pass
  
  def __processNOR(self, permissions, context, type = None):
    pass
  
  def __processXOR(self, permissions, context, type = None):
    pass
  
  def __processNOT(self, permissions, context, type = None):
    pass
  
  def __externalAccessCheck(self, permission, context, type):
    pass
