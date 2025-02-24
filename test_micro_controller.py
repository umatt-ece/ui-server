import can
from mcu_driver import Microcontroller

mc1 = Microcontroller()
mc2 = Microcontroller()

mc1.set("parameter1", "value1")

msg_received = mc2.get("parameter1")

msg_expected = can.Message(arbitration_id=0x123, data=[1, 2, 3])

assert msg_expected.arbitration_id == msg_received.arbitration_id
assert msg_expected.data == msg_received.data
assert msg_expected.timestamp != msg_received.timestamp  

mc1.close()
mc2.close()

print("Program end normally!")
