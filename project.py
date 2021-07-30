!pip install adafruit-io --quiet
# Import library and create instance of REST client.
from Adafruit_IO import Client
aio = Client('Manisha_Muntha', 'aio_QSlx229PCW61B3lhuxqKVw88HR1h')

# Send the value 1 to a feed called 'Foo'.
aio.send('bedroom-light',1)
aio.send('fan',1 )

# Retrieve the most recent value from the feed 'Foo'.
# Access the value by reading the `value` property on the returned Data object.
# Note that all values retrieved from IO are strings so you might need to convert
# them to an int or numeric type if you expect a number.
data1 = aio.receive('bedroom-light')
data2 = aio.receive('fan')
print(f'Received value: {data1.value}')
print(f'Received value: {data2.value}')

