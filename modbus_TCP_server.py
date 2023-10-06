# Modbus server (TCP)
from pymodbus.server import StartTcpServer, StartAsyncTcpServer, ServerAsyncStop, ServerStop
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder
from pymodbus.constants import Endian
from pymodbus.datastore import ModbusSparseDataBlock
import time
import random
import threading

port = 502  # port number

address=0 # starting address of the registers

# Temperature sensor data
temps = [10.0, 5.21 , 1.75 , -4 , 53.3 , 27.132, 16.96 , -28 , 31.1 , 4.3]

#get the current time in seconds 
start = time.time()

def read_registers(address, registers,func_context):
    # decode the values from the context using the address and the number of registers, the values are stored in a list
    # funcion code to read holding registers is 0x03
    decoder = BinaryPayloadDecoder.fromRegisters(func_context[0].getValues(fc_as_hex=0x03, address=address, count=2*len(temps)), byteorder=Endian.BIG, wordorder=Endian.LITTLE)
    # store the decoded values in a list, requires a buffer of 4 bytes (32 bits) to unpack the float value from the registers
    values = [decoder.decode_32bit_float() for i in range(registers)]
    # round down to the nearest two decimal places
    values = [round(i,5) for i in values]
    return values

def write_registers(address,context_func,values,builder):
    # insert a random value to the builder (32 bits) after resetting the builder
    builder.reset()
    for i in range(len(values)):
        builder.add_32bit_float(values[i])
    # convert the builder to a list of registers
    payload = builder.to_registers()
    # insert the values to the context in a random address in the range of address to address+len(temps)
    context_func[0].setValues(fc_as_hex=0x10, address=address, values=payload)

def start_operations(values=[0]*10):
    # make builder to pass values to the context as a list of floats (32 bits)
    builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)
    # write the initial values to the context
    write_registers(address,context,values,builder)
    #print initial values
    print(f'Initial values: {read_registers(address, len(temps),context)}')
    while True: # keep server running
        try:
            time.sleep(1)
        except:
            break


def run_modbus_server(context_f):
    server = StartTcpServer(context=context_f, host='localhost',\
                   identity=identity, address=("127.0.0.1", 502))
    #check if the server is running
    
if __name__ == "__main__":
    nreg = 200 # number of registers
    # initialize data store
    store = ModbusSlaveContext(
    hr=ModbusSparseDataBlock( {0 : [0]*nreg} )) # holding registers initialized to 0
    context = ModbusServerContext(slaves=store, single=True)
    # initialize the server information
    identity = ModbusDeviceIdentification()
    print(f'\nModbus server started on localhost port {port}')
    try:   
        start_operations(temps)
        run_modbus_server(context)
    except KeyboardInterrupt:
        print('\nModbus server stopped')

    

