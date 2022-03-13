import logging
from logging.config import fileConfig
from os import path
from collections import deque

# import the logging.ini file
basepath = path.dirname(__file__)
logging_ini_filepath = path.abspath(path.join(basepath, "..", "logging.ini"))
#logging_ini_filepath = "C:\\Users\\will9\\OneDrive\\Desktop\\git_code\\comp_arch_computer\\src\\simulator\\logging.ini"
fileConfig(logging_ini_filepath)
logger = logging.getLogger()


class MemoryData:
    def __init__(self, address, value):
        self.address = address
        self.value = value

class Memory(MemoryData):


    def __init__(self):
        self.word_length = 16
        self.memory_length = 2048
        self.cache_length = 2
        self.memory_data = list(MemoryData(i, None) for i in range(self.memory_length))
        self.cache = deque(MemoryData(None, None) for i in range(self.cache_length))
    

    def set(self, address:str, value:str, binary:bool):
        '''
        sets the memory to value given address. 
        Parameters:
        address:str
            address value must be a string value of either binary or decimal 
        value:str
            value to set the address to. must be string of either binary or decimal
        binary:bool
            True or False. True if address and values are binary strings
        Returns:
            Updates the memory with the given address and value
        '''
        assert isinstance(address, str)
        assert isinstance(value, str)

        if binary:
            address = int(address, 2)
            value = int(value, 2)
        else:
            address = int(address)
            value = int(value)

        if address < 6:
            logger.critical('Addresses less than 6 are prohibited as they are reserved spaces: address %s, value: %s' % (str(address), str(value)))
            raise Exception('Addresses less than 6 are prohibited as they are reserved spaces')

        # do we need logic for if the address is already set to another value? 

        if not address > self.memory_length or not value > 65536:
            
            # check if value already exists at this address. For now will continue to overwrite the value
            get_value = self.get(address, binary=False)
            if get_value is not None:
                logger.info('Value already exists at this address in memory. Will continue to overwrite this value.. Previous value: %s' % str(get_value))
            
            # set the address and value in cache
            self._add_to_cache(MemoryData(address, value))
            logger.info('address %s and value %s set in cache' % (str(address), str(value)))
            
            # set the vlaue to the memory
            setattr(self.memory_data[address], 'value', value)
            setattr(self.memory_data[address], 'address', address)
            logger.info('address %s and value %s set in memory' % (str(address), str(value)))
    

    def get(self, address:str, binary:bool):
        '''
        gets the value at the given address 
        Parameters:
        address:str
            address value must be a string value of either binary or decimal 
        binary:bool
            True or False. True if address and values are binary strings
        Returns:
            Updates the memory with the given address and value
        '''
        if binary: 
            address = int(address, 2)
        else: 
            address = int(address)
        
        if address < 6:
            logger.critical('Addresses less than 6 are prohibited as they are reserved spaces: address %s' % str(address))
            raise Exception('Addresses less than 6 are prohibited as they are reserved spaces')

        # try getting the value from the cache and if found, return it early and skip even checking the memory
        for cache_object in self.cache: 
            if address == cache_object.address:
                logger.debug(
                    "Value found in cache!"
                )
                return cache_object.value
            
        try: 
            value = getattr(self.memory_data[address], 'value')
        except Exception as e: 
            logger.debug('Exception occurs during retrieval of memory at address %s. Exception: %s' % (str(address), str(e)))

        if not value: 
            logger.debug('Either address is incorrect or is not set in memory for address %s' % (str(address)))
        return value
    
    
    def _add_to_cache(self, new_data):
        self.cache.appendleft(new_data)
        self.cache.pop()
        

    def expand_memory(self):
        'expand the memory to length of 4096'
        self.memory_length = 4096
        # expands the memory while preserving current memory
        self.memory_data = list(MemoryData(i, 0) for i in range(self.memory_length) if getattr(MemoryData, 'value', None))
        logger.info('memory expanded to %s' % str(self.memory_length))
    
    def shrink_memory(self):
        'shrink the memory to memory length of 2048'
        self.memory_length = 2048
        # shrinks the memory while preserving address values if they exist
        self.memory_data = list(MemoryData(i, 0) for i in range(self.memory_length) if getattr(MemoryData, 'value', None))
        logger.info('memory shrinked to %s' % str(self.memory_length))

    def get_word_length(self):
        'get current word length'
        return self.word_length
    
    def get_memory_length(self):
        'get the current capacity'
        return self.memory_length

    def dump_memory(self):
        pass