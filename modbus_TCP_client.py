from pymodbus.client import ModbusTcpClient as ModbusClient
from pymodbus.payload import BinaryPayloadDecoder, BinaryPayloadBuilder
from pymodbus.constants import Endian
import time

registers = 10
print('Start Modbus Client')

client = ModbusClient(host='127.0.0.1',port=502, source_address=('127.0.0.1',502), reuse_address=True)
starting_address = 0  # starting address of the registers

try:
    client.connect()
    if client.connected:
        print('Connected to the server')
except Exception as e:
    print(f'Error connecting to the server: {e}')
    exit()
def read_registers(starting_address, registers):
    # read the values from the server, the values are stored in a list of registers
    regs = client.read_holding_registers(address=starting_address,  count=registers,fc_as_hex=0x03).registers
    # initialize the decoder with the registers, the byteorder and the wordorder
    decoder = BinaryPayloadDecoder.fromRegisters(registers=regs, byteorder=Endian.BIG, wordorder=Endian.LITTLE)
    # store the decoded values in a list, requires a buffer of 4 bytes (32 bits) to unpack the float value from the registers
    values = [decoder.decode_32bit_float() for i in range(registers)]
    values = [round(i, 2) for i in values]
    print(values)
    return values
 
try:
    values = read_registers(starting_address, registers)
    print(f'Values read: {values}')
    time.sleep(1)
except KeyboardInterrupt:
    client.close()

print('\nEnd Modbus Client')
