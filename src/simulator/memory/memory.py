<<<<<<< HEAD
import logging
from logging.config import fileConfig
from os import path

# import the logging.ini file
basepath = path.dirname(__file__)
logging_ini_filepath = path.abspath(path.join(basepath, "..", "logging_config.ini"))
fileConfig(logging_ini_filepath)
logger = logging.getLogger()


class MemoryData:
    def __init__(self, address, value):
        self.address = address
        self.value = value



class Memory(MemoryData):
    def __init__(self) -> None:
        self.word_length = 16
        self.memory_length = 2048
        self.memory_data = list(MemoryData(i, None) for i in range(self.memory_length))
    

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

        if not address > self.memory_length or not value > 65536:
            setattr(self.memory_data[address], 'value', value)
            logger.info('address %s and value %s set' % (str(address), str(value)))
    

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
        assert isinstance(address, str)
        if binary: 
            address = int(address, 2)
        else: 
            address = int(address)
        
        if address < 6:
            logger.critical('Addresses less than 6 are prohibited as they are reserved spaces: address %s' % str(address))
            raise Exception('Addresses less than 6 are prohibited as they are reserved spaces')

        try: 
            value = getattr(self.memory_data[address], 'value')
        except Exception as e: 
            logger.debug('Exception occurs during retrieval of memory at address %s. Exception: %s' % (str(address), str(e)))

        if value is None:
            logger.info('Value at %s address is not set. Value is %s' % (str(address), str(value)))
        else: 
            return value



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

    
=======
>>>>>>> a23cdcfb7dd7d5366c05fe73940a430ecf5f6299

